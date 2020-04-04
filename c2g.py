import os
from os import system, name
from time import sleep

def isiSerial():   
    myfile = open("bank_serial.txt", "r")
    serial = myfile.readlines()
    print (serial[x])
    serialW = open("serial.txt", "w")
    serialW.writelines(serial[x])
    myfile.close()
    

def mvSerial():
    if x == 0:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO1')
        print('Serial berhasil tercopy ke GSC 1')
        os.system('mv /home/deddy/Documents/gsc/1/* /media/deddy/GRAFINDO1')
        print('Database berhasil tercopy ke GSC 1')
    elif x == 1:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO2')
        print('Serial berhasil tercopy ke GSC 2')
        os.system('mv /home/deddy/Documents/gsc/2/* /media/deddy/GRAFINDO2')
        print('Database berhasil tercopy ke GSC 2')
    elif x == 2:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO3')
        print('Serial berhasil tercopy ke GSC 3')
        os.system('mv /home/deddy/Documents/gsc/3/* /media/deddy/GRAFINDO3')
        print('Database berhasil tercopy ke GSC 3')
    elif x == 3:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO4')
        print('Serial berhasil tercopy ke GSC 4')
        os.system('mv /home/deddy/Documents/gsc/4/* /media/deddy/GRAFINDO4')
        print('Database berhasil tercopy ke GSC 4')
    elif x == 4:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO5')
        print('Serial berhasil tercopy ke GSC 5')
        os.system('mv /home/deddy/Documents/gsc/5/* /media/deddy/GRAFINDO5')
        print('Database berhasil tercopy ke GSC 5')
    elif x == 5:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO6')
        print('Serial berhasil tercopy ke GSC 6')
        os.system('mv /home/deddy/Documents/gsc/6/* /media/deddy/GRAFINDO6')
        print('Database berhasil tercopy ke GSC 6')
    elif x == 6:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO7')
        print('Serial berhasil tercopy ke GSC 7')
        os.system('mv /home/deddy/Documents/gsc/7/* /media/deddy/GRAFINDO7')
        print('Database berhasil tercopy ke GSC 7')
    elif x == 7:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO8')
        print('Serial berhasil tercopy ke GSC 8')
        os.system('mv /home/deddy/Documents/gsc/8/* /media/deddy/GRAFINDO8')
        print('Database berhasil tercopy ke GSC 8')
    elif x == 8:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO9')
        print('Serial berhasil tercopy ke GSC 9')
        os.system('mv /home/deddy/Documents/gsc/9/* /media/deddy/GRAFINDO9')
        print('Database berhasil tercopy ke GSC 9')
    elif x == 9:
        os.system('mv /home/deddy/Documents/Experiment-python/serial.txt /media/deddy/GRAFINDO10')
        print('Serial Berhasil tercopy ke GSC 10')
        os.system('mv /home/deddy/Documents/gsc/10/* /media/deddy/GRAFINDO10')
        print('Database berhasil tercopy ke GSC 10')
    else:
        print('tidak ada data')


def copyEbook():

    path = '/media/deddy'

    for filename in os.listdir(path):
        src = '/home/deddy/Documents/SDCARD-New-Version/ORDER/AL-MUHAJIRIN/SO1020017363500002/*'
        dst = path+'/'+filename
    
        os.system('cp -R %s %s' % (src, dst))


def clear():
    if name == 'int':
        _ = system('cls')
    else:
        _ = system('clear')



clear()
awal = 0
akhir = int(input('input jumlah GSC = '))
for x in range(awal,akhir):
    #isiSerial()
    #mvSerial()
    #copyEbook()
    print(x)




