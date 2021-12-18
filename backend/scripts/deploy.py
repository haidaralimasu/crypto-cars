from os import access
from scripts.helpful_scripts import get_account
from brownie import CarBattle

def deploy_car_battel():
    account = get_account()
    car_battle = CarBattle.deploy({"from":account}, publish_source=True)
    print(car_battle.address)

def main():
    deploy_car_battel()