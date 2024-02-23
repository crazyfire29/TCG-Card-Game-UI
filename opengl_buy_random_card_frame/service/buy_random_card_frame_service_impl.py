from opengl_buy_random_card_frame.entity.buy_random_card_scene import BuyRandomCardScene
from opengl_buy_random_card_frame.frame.buy_random_card_frame import BuyRandomCardFrame
from opengl_buy_random_card_frame.service.buy_random_card_frame_service import BuyRandomCardFrameService
from card_shop_frame.frame.buy_check_frame.service.request.buy_random_card_request import BuyRandomCardRequest
from opengl_button.button_binding.buy_random_card_button_bind import BuyRandomCardFrameButtonBind

from session.repository.session_repository_impl import SessionRepositoryImpl
from card_shop_frame.frame.buy_check_frame.repository.buy_check_repository_impl import BuyCheckRepositoryImpl


class BuyRandomCardFrameServiceImpl(BuyRandomCardFrameService):
    __instance = None
    __transmitIpcChannel = None
    __receiveIpcChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__buyRandomCardFrame = BuyRandomCardFrame
            cls.__instance.__buyRandomCardScene = BuyRandomCardScene()
            cls.__instance.__sessionRepository = SessionRepositoryImpl.getInstance()
            cls.__instance.__buyCheckRepository = BuyCheckRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        self.card_numbers = None



    def findRandomCardNumbers(self, card_numbers):
        print(f"card_numbers: {card_numbers}")
        self.card_numbers = card_numbers
        self.__buyRandomCardFrame().set_random_card_numbers(self.__buyCheckRepository.getRandomCardList())
        self.createBuyRandomCardUiFrame(rootWindow, switchFrameWithMenuName)

    def createBuyRandomCardUiFrame(self, rootWindow, switchFrameWithMenuName):
        buyRandomCardrame = self.__buyRandomCardFrame(rootWindow)
        buyRandomCardrame.set_random_card_numbers(self.__buyCheckRepository.getRandomCardList())
        print(f"buyRandomCardrame.random_card_numbers: {buyRandomCardrame.random_card_numbers}")

        buttonBinding = BuyRandomCardFrameButtonBind(master=rootWindow, frame=buyRandomCardrame)
        buttonBinding.button_bind()

        return buyRandomCardrame
