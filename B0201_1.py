import time
start = time.perf_counter()
my_list = list(range(10_000_000))
end = time.perf_counter()
duration = end - start
print(f"Waktu yang dibutuhkan untuk membuat list 10 juta elemen adalah {duration:.6f} detik")
