"""En el siguiente codigo se realiza la conversion
ede Megabytes a:
-- bits
-- Bytes
-- Kilobytes
-- Gigabytes"""

megab = float(input("digite el numero de Megabytes a convertir: "))
bits = megab * 8388606
bytes = megab * 1048576
kb = megab * 1024
gb = megab * 0.000976563
print(megab, "megabytes equivale a: ", bits, " bits")
print(megab, "megabytes equivale a: ", bytes, " bytes")
print(megab, "megabytes equivale a: ", kb, " kilbytes")
print(megab, "megabytes equivale a: ", gb, " Gygabytes")
