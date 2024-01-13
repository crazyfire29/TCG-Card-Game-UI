from account_register_frame.service.account_register_frame_service_impl import AccountRegisterFrameServiceImpl
from app_window.service.window_service_impl import WindowServiceImpl
from account_login_frame.service.login_menu_frame_service_impl import LoginMenuFrameServiceImpl
from main_frame.service.main_menu_frame_service_impl import MainMenuFrameServiceImpl
from ui_frame.controller.ui_frame_controller import UiFrameController
from ui_frame.service.ui_frame_service_impl import UiFrameServiceImpl


class UiFrameControllerImpl(UiFrameController):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__uiFrameService = UiFrameServiceImpl.getInstance()
            cls.__instance.__windowService = WindowServiceImpl.getInstance()
            cls.__instance.__mainMenuFrameService = MainMenuFrameServiceImpl.getInstance()
            cls.__instance.__loginMenuFrameService = LoginMenuFrameServiceImpl.getInstance()
            cls.__instance.__accountRegisterFrameService = AccountRegisterFrameServiceImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def requestToCreateUiFrame(self):
        print("UiFrameControllerImpl: requestToCreateUiFrame()")

        self.__windowService.createRootWindow()
        rootWindow = self.__windowService.getRootWindow()

        mainMenuFrame = self.__mainMenuFrameService.createMainUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerMainMenuUiFrame(mainMenuFrame)

        loginMenuFrame = self.__loginMenuFrameService.createLoginUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerLoginMenuUiFrame(loginMenuFrame)

        accountRegisterFrame = self.__accountRegisterFrameService.createAccountRegisterUiFrame(rootWindow)
        self.__uiFrameService.registerAccountRegisterUiFrame(accountRegisterFrame)

        self.switchFrameWithMenuName("main-menu")

    def switchFrameWithMenuName(self, name):
        print("UiFrameControllerImpl: switchFrameWithMenuName()")
        self.__uiFrameService.switchFrameWithMenuName(name)

    def requestToStartPrintGameUi(self):
        print("UiFrameControllerImpl: requestToStartPrintGameUi()")
        rootWindow = self.__windowService.getRootWindow()
        rootWindow.mainloop()

    def requestToInjectTransmitIpcChannel(self, transmitIpcChannel):
        print("UiFrameControllerImpl: requestToInjectTransmitIpcChannel()")
        self.__uiFrameService.injectTransmitIpcChannel(transmitIpcChannel)


