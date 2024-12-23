# ssr switch by gpio on raspberry pi

![20210821150402](https://github.com/user-attachments/assets/641a7cab-0a96-4d4b-83ef-745ea7f69533)

## 1 non-threading

ssr_main8.py -> ssr_sw_class.py

## 1 threading

ssr_th_main.py -> ssr_sw_th.py -> ssr_sw_class.py

## ssr_th_main.py usage (threading)

start: python3 ssr_th_main.py 8 2 2

where the first 8 is pin number, the second 2 is "on time", the last 2 is "off time"

touch 8go.txt: make ssr contorl active

rm 8go.txt: make ssr contorl inactive

control-C stop this program

## check thread name

python3 thname.py

## 2 threading

ssr_th_main2.py -> ssr_sw_th.py -> ssr_sw_class.py

## ssr_th_main2.py usage (threading)

start: python3 ssr_th_main2.py

## GPIOs test with LEDs

### 11,12,13,15,16,18 = GPIO pin No. on Raspberry Pi board

python3 gpio_test.py

### References

threading — Thread-based parallelism — Python 3.13.0 documentation

https://docs.python.org/3/library/threading.html
