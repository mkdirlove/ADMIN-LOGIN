### ADMIN PANEL LOGIN LOGIN ###

import os
import sys
import getpass
from time import sleep

def tampil(x):
        w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36,'p':37}
        for i in w:
                x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
        x+='\033[0m'
        x=x.replace('\r0','\033')
        print(x)

def berhasil():
        os.system('clear')
        os.system('figlet -f slant " LOGIN" | lolcat')
        os.system('figlet -f slant "SUCCESFUL" | lolcat')
        os.system('sleep 3')
        os.system('clear')
        print (" ")
        tampil ('         [][][][][][][][][][][][][][][][][][][][]')
	os.system('sleep 1')
	tampil ('              ADMIN    >\rh @@@@@@@@@@')
        os.system('sleep 1')
        tampil ('              USERNAME >\rh @@@@@@@@@@')
	os.system('sleep 1')
	tampil ('              ID       >\rh @@@@@@@@@@')
	os.system('sleep 1')
        tampil ('         [][][][][][][][][][][][][][][][][][][][]')
	os.system('sleep 3')
        os.system('clear')
	os.system('sleep 1')
        exit()

def salah():
	os.system('clear')
	tampil (' ')
	os.system('figlet -f slant " LOGIN" | lolcat')
	os.system('figlet -f slant " FAILED" | lolcat')
	os.system('sleep 2')
	tampil (' ')
	tampil (' [!] \rmWRONG USERNAME OR PASSWORD')
	os.system('sleep 1')
	tampil (' [*] \rhTRY AGAIN!!')
	os.system('sleep 3')
	os.system('clear')

def login():
        keep_asking = True
        while keep_asking:
                try:
			tampil ('''
\rm
@@@  @@                                   @@  @@@
  @@@@@@                                 @@@@@@
   @@@@@           88888888888           @@@@@
     @@@@        888888888888888        @@@@
       @@@@    8888888888888888888    @@@@
         @@@@88888888888888888888888@@@@
            8888  888888888888  88888@
           88888    88888888    888888
           88888      8888      888888
            8888888888888888888888888
             88888888888  8888888888
               8888888      888888
                 888888888888888
                 @8888888888888@
               @@@@|||||||||||@@@@
             @@@@  |||||||||||  @@@@
           @@@@                   @@@@
        @@@@@                       @@@@@
       @@  @@@                     @@@  @@''')
			print ('\033[31;1m==========================================================')
			print ('''\033[31;1m@@@@@@   @@@@  @@@@@@  @@  @@     @@     @@ @@   @@ @@  @@
 @@  @@ @@  @@  @@  @@ @@ @!      @@     @@ @@@  @@ @@ @!
 @@  @! @@@@@@  @@@@@  @@!    @!! @@     @@ @@ @ @! @@@!
 @!  !! @!  !!  @! @!  @! !!      @!     @! @!  @!! @! !!
!!!!!!  !!  !!  !!  !! !!  !!     !!!!!! !! !!   !! !!  !!
 ! !!   !    !  !    ! !    !      !! !  !  !     ! !    !
\033[31;1m==========================================================\033[32;1m''')
                        user = raw_input('\033[32;1m>>> Username__ \033[30;1m')
                        sandi = getpass.getpass('\033[32;1m>>> Password__ ')
                        if sandi == 'SSAANNDDII' and user == 'UUSSEERR':
                                berhasil()
                        else:
				salah()
		except KeyboardInterrupt:
                        tampil ('\rp[*] KEYBOARDINTERRUPT DETECTED')
			os.system('sleep 1')
			tampil ('\rp[!]\rm CAN`T KEYBOARDINTERRUPT')
			sleep(3)
			os.system('clear')
                        login()
                except NameError:
                        login()
                except ValueError:
                        login()

os.system('clear')
login()
