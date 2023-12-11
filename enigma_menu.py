# Python Menu System for Enigma 2
# NetAlly 2023

def product_code_menu():
    """
    Displays a menu to select a product code and directs to the corresponding option menu.
    Returns:
        tuple: Selected product code and the corresponding option code.
    """

    menu = '''
            1.) 6964 - OneTouch AT
            2.) 6963 - EtherScope/MetroScope
            3.) 7001 - LinkRunner Pro Duo
            4.) 2186 - OptiView XG
            5.) 1890 - ClearSight Analyzer
            6.) 1895 - iClearSight Analyzer
            7.) 3001 - Nettool S2
            8.) Product Code Not Listed
        '''
    print(menu)
    while True:
        choice = input("Choose your option: ")
        if choice == '1':
            return '6964', onetouch_option_menu()
        elif choice == '2':
            return '6963', etherscope_menu()
        elif choice == '3':
            return '7001', linkrunner_menu()
        elif choice == '4':
            return '2186', optiviewxg_menu()
        elif choice == '5':
            return '1890', clearsight_menu()
        elif choice == '6':
            return '1895', i_clearsight_menu()
        elif choice == '7':
            return '3001', nettools2_menu()
        elif choice == '8':
            product_code = input('Please Enter Product Code: ')
            option_code = input("Please Enter Option Code: ")
            return product_code, option_code
        else:
            print("Invalid choice. Please try again.")


def onetouch_option_menu():
    """
    Displays the OneTouch AT option menu for product code 6964.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - Registered
        1.) 001 - Wired (Was Copper)
        2.) 002 - Obsolete (was fiber)
        3.) 003 - Wi-Fi
        4.) 004 - Obsolete (was inline)
        5.) 005 - Capture
        6.) 006 - Advanced Tests 
        7.) 007 - XGR-to-ATX Upgrade (only set when a PTR is programmatically converted to a 10G)
        8.) 008 - Claimed (set when a unit is claimed for cloud tools, but the "real" claim data is in the cloud backend)
        9.) 009 - LatTests (GB/T 21671 China LAN Acceptance Test specific performance tests; for China market only)
        64.) 064 - XGReflector (Future)
        65.) 065 - Performance Peer (Future)
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '64', '65']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return choice.zfill(3)  # Ensure the option code is three digits
        else:
            print("Invalid choice. Please try again.")


def etherscope_menu():
    """
    Displays the EtherScope/MetroScope option menu for product code 6963.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - MetroScope Base, EtherScope LAN
        1.) 001 - MetroScope WLAN, EtherScope WLAN
        2.) 002 - MetroScope Multi, EtherScope ITO
        3.) 003 - MetroScope VoIP, EtherScope Fiber
        4.) 004 - MetroScope LT, EtherScope LT
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1', '2', '3', '4']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return choice.zfill(3)  # Ensure the option code is three digits
        else:
            print("Invalid choice. Please try again.")


def linkrunner_menu():
    """
    Displays the LinkRunner Pro Duo option menu for product code 7001.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - 802.1x
        1.) 001 - Reports
        2.) 002 - LAN
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1', '2']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return choice.zfill(3)  # Ensure the option code is three digits
        else:
            print("Invalid choice. Please try again.")


def optiviewxg_menu():
    """
    Displays the OptiView XG option menu for product code 2186.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - Wireless Analyzer Option
        1.) 001 - Enables Network Test Ports A - D
        2.) 002 - 10Gb Ethernet Analyzer Option
        3.) 003 - LAN / 10Gb Ethernet Analyzer Option
        4.) 004 - NPT - Network Performance Option
        7.) 007 - Everything (I THINK)
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1', '2', '3', '4', '7']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return choice.zfill(3)  # Ensure the option code is three digits
        else:
            print("Invalid choice. Please try again.")


def clearsight_menu():
    """
    Displays the ClearSight Analyzer option menu for product code 1890.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - Activation Code
        1.) 007 - All Options
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return '007' if choice == '1' else '000'  # Mapping choice to the respective option code
        else:
            print("Invalid choice. Please try again.")


def i_clearsight_menu():
    """
    Displays the iClearSight Analyzer option menu for product code 1895.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        0.) 000 - Activation Code
        1.) 003 - All Options
    '''
    print(menu)

    # Valid options
    valid_options = ['0', '1']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return '003' if choice == '1' else '000'  # Mapping choice to the respective option code
        else:
            print("Invalid choice. Please try again.")


def nettools2_menu():
    """
    Displays the NetTools S2 option menu for product code 3001.
    Returns:
        str: Selected option code as a three-digit string.
    """
    # Displaying the menu options
    menu = '''
        3.) 003 - Personalization
        4.) 004 - VoIP
        5.) 005 - NetSecure
        8.) 008 - Dicom
    '''
    print(menu)

    # Valid options
    valid_options = ['3', '4', '5', '8']

    while True:
        choice = input("Choose your option: ")
        if choice in valid_options:
            return choice.zfill(3)  # Ensure the option code is three digits
        else:
            print("Invalid choice. Please try again.")
