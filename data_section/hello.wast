(module
  (type (;0;) (func (result i32)))
  (func (;0;) (type 0) (result i32)
    i32.const 16)
  (table (;0;) 0 funcref)
  (memory (;0;) 1)
  (export "memory" (memory 0))
  (export "hello" (func 0))
  (data (;0;) (i32.const 16) "hello from WebAssembly !\00"))
