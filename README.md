# ssr-switch-by-gpio-on-raspberry_py
ssr switch by gpio on raspberry_py

![20210821150402](https://github.com/user-attachments/assets/641a7cab-0a96-4d4b-83ef-745ea7f69533)

## 1 non-threading

ssr_main8.py -> ssr_sw_class.py

## 2 threading

ssr_th_main.py -> ssr_sw_th.py -> ssr_sw_class.py

## ssr_th_main.py usage (threading)

start: python3 ssr_th_main.py 8 2 2

where the first 8 is pin number, the second 2 is "on time", the last 2 is "off time"

touch 8go.txt: make ssr contorl active

rm 8go.txt: make ssr contorl inactive

control-C stop this program
