from asyncio import ALL_COMPLETED

import aiohttp
import requests
import time
import asyncio


class CurrencyAPI:
    cache = {}

    def __init__(self, api_key, api_name):
        self.api_key = api_key
        self.api_name = api_name

    @classmethod
    def set_to_cache(cls, key, value):
        cls.cache[key] = value

    @classmethod
    def get_from_cache(cls, key):
        try:
            return cls.cache[key]
        except KeyError:
            return None

    @staticmethod
    async def status_code(status_code: int):
        if status_code == 200:
            print('Status code 200: Success!!!')
        elif status_code == 404:
            print('Error 404: Wrong URL!!!')
        elif status_code == 428:
            print('Let\'s wait 4 seconds')
            asyncio.sleep(4)

    def __repr__(self):
        return f"CurrencyAPI(api_key='{self.api_key}', api_name='{self.api_name}"


class MonoAPI(CurrencyAPI):
    def __init__(self, api_name, api_key, url, data=None):
        super().__init__(api_name, api_key)
        self.url = url
        self.data = data

    async def get_currency(self):
        try:
            if self.get_from_cache('Mono_curr_rate'):  # якщо у файлі cache['Privat_curr_rate'] щось є:
                self.data = self.cache['Mono_curr_rate'].json()  # об'єкт response перетворюємо у json
                print('Receive MonoBank CACHE data!')
                await self.parsing_data('USD', 'UAH')
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url) as response:
                        self.data = await response.json()  # об'єкт response перетворюємо у json
                        print('Receive MonoBank API data!')
                        await self.status_code(response.status)
                        await self.parsing_data('USD', 'UAH')
        except aiohttp.ClientError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as e:
            print(f'Something goes wrong: {e}')

    async def parsing_data(self, curr1_name, curr2_name):
        curr_codes = {'USD': 840, 'EUR': 878, 'UAH': 980}
        codeA = curr_codes[curr1_name]
        codeB = curr_codes[curr2_name]
        for curr in self.data:
            if curr["currencyCodeA"] == codeA and curr["currencyCodeB"] == codeB:
                print(f'Data obtained:\n\tCurrencyA: {curr1_name}\n\tCurrencyB: {curr2_name}\n\t'
                      f'rateBuy: {curr["rateBuy"]}\n\trateSell: {curr["rateSell"]}')


class PrivatAPI(CurrencyAPI):
    def __init__(self, api_name, api_key, url, data=None):
        super().__init__(api_name, api_key)
        self.url = url
        self.data = data

    async def get_currency(self):
        try:
            if self.get_from_cache('Privat_curr_rate'):  # якщо у файлі cache['Privat_curr_rate'] щось є:
                self.data = self.cache['Privat_curr_rate'].json()  # об'єкт response перетворюємо у json
                print('Received PrivatBank CACHE data!')
                await self.parsing_data('USD', 'UAH')
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url) as response:
                        self.data = await response.json()  # об'єкт response перетворюємо у jso
                        print('Received PrivatBank API data!')
                        await self.status_code(response.status)
                        await self.parsing_data('USD', 'UAH')
        except aiohttp.ClientError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as e:
            print(f'Something goes wrong: {e}')

    async def parsing_data(self, curr1_name, curr2_name):
        for curr in self.data:
            if curr["ccy"] == curr1_name and curr["base_ccy"] == curr2_name:
                print(f'Data obtained:\n\tCurrencyA: {curr1_name}\n\tCurrencyB: {curr2_name}\n\t'
                      f'rateBuy: {curr["buy"]}\n\trateSell: {curr["sale"]}')


async def main():
    start = time.time()
    curr_mono = MonoAPI('Monobank', '', 'https://api.monobank.ua/bank/currency')
    curr_privat = PrivatAPI('PrivatBank', '', 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

    task1 = asyncio.create_task(curr_mono.get_currency())
    task2 = asyncio.create_task(curr_privat.get_currency())

    await asyncio.gather(task1, task2)
    print(time.time() - start)


asyncio.run(main())

