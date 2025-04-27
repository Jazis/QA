from models.user import User

USER_01 = User(password="vnLmdAxGAa4ZPeA6", login="admin@admin.com")

USER_RU = User(password="hfgyTRVVCDSWQ@$%", login="russianLanguige@mail.ru")

USER_UK = User(password="hfgyTRVVCDSWQ@$%", login="ukrainlanguige@mail.ru")

USER_EN = User(password="hfgyTRVVCDSWQ@$%", login="englishlanguige@mail.ru")

USER_DATA_RU = User(password="Hihu&hjghgf#hJKIUY&*bJHH", login="rtuuyhgfytr45fghfh@yandex.ru")

USER_DATA_RU_EMPLOYEE = User(password="SFHt57jhgojklj", login="invaited@mail.ru")

USER_BLACK_COMPANY = User(password="BLaCKCOMPAny2010", login="blackCompany@mail.ru")

USER_WHITE_COMPANY = User(password="whiteCompany@mail.ru", login="whiteCompany@mail.ru")

USER_WHITE_COMPANY_EMPLOYEE = User(password="whiteCompany@mail.ru", login="someemail@google.com")

USER_GREY_COMPANY = User(password="GREY_CompAny2012", login="greyCompany@mail.ru")

USER_DISABLED_COMPANY = User(password="egert546qa7y4a56etjfyjkxhgkj", login="testDisabledCompamy@mail.ru")

USER_DISABLED_EMPLOYEE = User(password="egert546qa7y4a56etjfyjkxhgkj", login="testdisabledemployee@mail.ru")

USER_RESTRICTED_COMPANY = User(password="egert546qa7y4a56etjfyjkxhgkj", login="testRestictededCompamy@mail.ru")

USER_RESTRICTED_EMPLOYEE = User(password="3453trgfbnjyhy5t4r3edwefsg", login="testRestrictedEmployee@mail.ru")

USER_NOT_ACTIVATED_COMPANY = User(password="dkljgklarjfo8eu458934tiorea", login="doNotActivateRU+2@kjgdkl.ru") #ru

USER_NOT_ACTIVATED_COMPANY_EN = User(password="pAwQBtjuY", login="haSC@gmail.com")

USER_NOT_ACTIVATED_COMPANY_UK = User(password="dgerytruyfjhgjmc", login="doNotActivateUK@mail.ru")

USER_RUBY_ROSE = User(password="rYBuRose2020", login="rubyRose@mail.ru") #RU

FAKE_VALID_USERS = [
    User(password="udak7nsv7wwctjgqwe", login="admin@admin.com"),
    User(password="UdAK7nSV7WWCtjGddd", login="admin+1@admin.com"),
    User(password="UdAK7snSVwwCtjG", login="admin@admin.com"),
    User(password="UdAK7n sSV7WWCtjG", login="admin@admin.com"),
    User(password="UdAK7nSaV7WWCtjG", login="admin@admin.com"),
    User(password="GDSgdfsaruherEWRWERfse", login="admin@admin.com"),
    User(password="UdAK7nSd&*()V7WWCtjG", login="admin@admin.com"),
    User(password="UdAK7enSV7WWCtjG", login="admn@admin.com "),
]

FAKE_INVALID_USERS = [
    User(password="UdAK7nfSV7WWCtjG", login=" "),
    User(password="UdAK7nfSV7WWCtjG", login="adm in@admin.com "),
    User(password="UdAK7nfSV7WWCtjG", login="admn@admin."),
    User(password="UdAK7nfSV7WWCtjG", login="admn@admincom"),
    User(password="UdAK7nfSV7WWCtjG", login="admnadmin.com"),
    User(password="UdAK7nfSV7WWCtjG", login="@admin.com"),
    User(password="UdAK7nfSV7WWCtjG", login="ad@min@admin.com")
]

VALID_USERS_WITH_ROLES = [
    User(password="hfgyTRVdVCDSWQ@$%", login="englishlanguige@mail.ru", role = "Viewer"),
    User(password="vnLmdAxGeAa4ZPeA6", login="admin@admin.com", role = "Admin"),
    User(password="CustomerSuccesrs21012024!@#$%^&*()", login="customer_success_dashboard@mail.ru", role = "CS"),
    User(password="Finance@@@d@@dQQWQEWEWE2324", login="financedashboard@mail.ru", role = "Finance"),
]