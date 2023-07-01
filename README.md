# layerzero-mim-tx-counter

Скрипт для получения количества MIM транзакий в abracadabra

Установка зависимостей: ```pip install requests```

- `wallets.txt` для записи кошельков (только адреса)
- `api_key` нужно получить на `https://ftmscan.com/myapikey` и подставить в файле `main.py`
- `offset` максимальное количество транзакций, которое будет выгружено для каждого кошелька, автоматически подставлено `1000` штук

В файле `results.txt` будет записан ответ в формате:

<pre><code>wallet1: 33
wallet2: 59
wallet3: 42</code></pre>