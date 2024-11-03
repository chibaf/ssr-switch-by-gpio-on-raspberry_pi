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

## check thread name

<pre>
pi@RasPi4B32BIT:~ $ python3 thname.py <br>
test<br>
test_thread<br>
</pre>

<pre>
import threading<br>
<br>
def test():<br>
    print("test")
</pre>
<pre>                                                              
thread = threading.Thread(target=test, name="test_thread")<br>
t.start()                              # Thread name<br>
t.join()<br>
print(t.name) # Here<br>
You can get the thread name test_thread as shown below:<br>
<br>
test<br>
test_thread # Here<br>
</pre>
