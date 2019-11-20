from wasmer import Module


print('[+] JOB START !!')
with open("payload.html", "rb") as payload, open("hello.wasm", "rb") as old_module, open("wasm_polyglot_custom.wasm", "wb") as new_module:
    ## wasm header
    wasm_header = b"\x00\x61\x73\x6D\x01\x00\x00\x00"
    
    ## retrieve html payload
    existing_payload = payload.read()
    print('[+] existing_payload = ' + str(existing_payload))

    ## retrieve old wasm module
    existing_module = old_module.read()
    print('[+] existing_module = ' + str(existing_module))
    ## remove wasm header from old_module
    existing_module = existing_module[8:]


    ## creation of the custom section fields
    wasm_custom_sec = b""
    custom_sec_id = b"\x00"
    name_len = b"\x00\x04"
    name = b'test'

    # bruteforce of the LEB128 length - just because i'm lazy.
    for i in range(0x00, 0xff):
        for j in range(0x00, 0xff):
            wasm_custom_sec = custom_sec_id + bytes([i]) + bytes([j]) + name_len + name + existing_payload
            ## Check if wasmer consider the custom section valid
            if Module.validate(wasm_header + wasm_custom_sec):
                ## custom section valided, write final module
                new_module.write(wasm_header + wasm_custom_sec + existing_module)
                print("[+] JOB DONE !!")
                exit()

print("[-] JOB FAILED !!")
