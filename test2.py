class Foydalanuvchi:
    def __init__(self, id, login, parol, ism, rol):
        self.id = id
        self.login = login
        self.parol = parol
        self.ism = ism
        self.rol = rol

class Oqituvchi(Foydalanuvchi):
    def __init__(self, id, login, parol, ism):
        super().__init__(id, login, parol, ism, 'oqituvchi')
        self.guruhlar = []

class Oquvchi(Foydalanuvchi):
    def __init__(self, id, login, parol, ism):
        super().__init__(id, login, parol, ism, 'oquvchi')
        self.guruh_id = None
        self.baholar = {}

class Admin(Foydalanuvchi):
    def __init__(self, id, login, parol, ism):
        super().__init__(id, login, parol, ism, 'admin')

class Guruh:
    def __init__(self, id, nomi, kurs):
        self.id = id
        self.nomi = nomi
        self.kurs = kurs
        self.oqituvchi_id = None
        self.oquvchilar = []

class Markaz:
    def __init__(self):
        self.foydalanuvchilar = {}
        self.oqituvchilar = {}
        self.oquvchilar = {}
        self.adminlar = {}
        self.guruhlar = {}
        self.keyingi_id = 1
        self.keyingi_guruh_id = 1
        self._demo_malumot()

    def _keyingi(self):
        i = self.keyingi_id
        self.keyingi_id += 1
        return i

    def _keyingi_guruh(self):
        i = self.keyingi_guruh_id
        self.keyingi_guruh_id += 1
        return i

    def _demo_malumot(self):
        a = Admin(self._keyingi(), 'admin', 'admin', 'Bosh Admin')
        self.foydalanuvchilar[a.login] = a
        self.adminlar[a.id] = a
        t = Oqituvchi(self._keyingi(), 't1', 't1', 'Oqituvchi Said1')
        self.foydalanuvchilar[t.login] = t
        self.oqituvchilar[t.id] = t
        s = Oquvchi(self._keyingi(), 's1', 's1', 'Oquvchi Said2')
        self.foydalanuvchilar[s.login] = s
        self.oquvchilar[s.id] = s
        g = Guruh(self._keyingi_guruh(), 'Python-1', 'Python boshlangich')
        self.guruhlar[g.id] = g
        g.oqituvchi_id = t.id
        t.guruhlar.append(g.id)
        g.oquvchilar.append(s.id)
        s.guruh_id = g.id

    def login_qil(self, login, parol):
        if login in self.foydalanuvchilar:
            f = self.foydalanuvchilar[login]
            if f.parol == parol:
                return f
        return None

    def oqituvchi_qosh(self, login, parol, ism):
        if login in self.foydalanuvchilar:
            return None, 'Bu login band.'
        i = self._keyingi()
        t = Oqituvchi(i, login, parol, ism)
        self.foydalanuvchilar[login] = t
        self.oqituvchilar[i] = t
        return t, 'Oqituvchi qoshildi.'

    def oquvchi_qosh(self, login, parol, ism):
        if login in self.foydalanuvchilar:
            return None, 'Bu login band.'
        i = self._keyingi()
        s = Oquvchi(i, login, parol, ism)
        self.foydalanuvchilar[login] = s
        self.oquvchilar[i] = s
        return s, 'Oquvchi qoshildi.'

    def guruh_yarat(self, nomi, kurs):
        gid = self._keyingi_guruh()
        g = Guruh(gid, nomi, kurs)
        self.guruhlar[gid] = g
        return g, 'Guruh yaratildi.'

    def guruhga_oqituvchi(self, guruh_id, oqituvchi_id):
        if guruh_id not in self.guruhlar:
            return 'Guruh topilmadi.'
        if oqituvchi_id not in self.oqituvchilar:
            return 'Oqituvchi topilmadi.'
        g = self.guruhlar[guruh_id]
        t = self.oqituvchilar[oqituvchi_id]
        if g.oqituvchi_id is not None:
            eski = self.oqituvchilar.get(g.oqituvchi_id)
            if eski and g.id in eski.guruhlar:
                eski.guruhlar.remove(g.id)
        g.oqituvchi_id = t.id
        if g.id not in t.guruhlar:
            t.guruhlar.append(g.id)
        return 'Oqituvchi biriktirildi.'

    def guruhga_oquvchi(self, guruh_id, oquvchi_id):
        if guruh_id not in self.guruhlar:
            return 'Guruh topilmadi.'
        if oquvchi_id not in self.oquvchilar:
            return 'Oquvchi topilmadi.'
        g = self.guruhlar[guruh_id]
        s = self.oquvchilar[oquvchi_id]
        if s.guruh_id is not None and s.guruh_id != guruh_id:
            eski = self.guruhlar.get(s.guruh_id)
            if eski and s.id in eski.oquvchilar:
                eski.oquvchilar.remove(s.id)
        s.guruh_id = g.id
        if s.id not in g.oquvchilar:
            g.oquvchilar.append(s.id)
        return 'Oquvchi guruhga qoshildi.'

    def mening_guruhlarim(self, oqituvchi_id):
        t = self.oqituvchilar.get(oqituvchi_id)
        if not t:
            return []
        return [self.guruhlar[gid] for gid in t.guruhlar if gid in self.guruhlar]

    def baho_qoy(self, oqituvchi_id, guruh_id, oquvchi_id, mavzu, ball):
        t = self.oqituvchilar.get(oqituvchi_id)
        if not t or guruh_id not in t.guruhlar:
            return 'Siz bu guruhga biriktirilmagansiz.'
        g = self.guruhlar.get(guruh_id)
        if not g or oquvchi_id not in g.oquvchilar:
            return 'Oquvchi ushbu guruhda emas.'
        s = self.oquvchilar.get(oquvchi_id)
        if not s:
            return 'Oquvchi topilmadi.'
        if mavzu not in s.baholar:
            s.baholar[mavzu] = []
        s.baholar[mavzu].append(ball)
        return 'Baho qoyildi.'

    def oquvchi_baholari(self, oquvchi_id):
        s = self.oquvchilar.get(oquvchi_id)
        if not s:
            return {}
        return s.baholar

    def oquvchi_ortacha(self, oquvchi_id):
        s = self.oquvchilar.get(oquvchi_id)
        if not s or not s.baholar:
            return 0.0
        jami = 0
        soni = 0
        for k in s.baholar:
            for b in s.baholar[k]:
                jami += b
                soni += 1
        if soni == 0:
            return 0.0
        return round(jami / soni, 2)

    def ro_yxat_oqituvchilar(self):
        return list(self.oqituvchilar.values())

    def ro_yxat_oquvchilar(self):
        return list(self.oquvchilar.values())

    def ro_yxat_guruhlar(self):
        return list(self.guruhlar.values())

def chiziq():
    print('-' * 60)

def asosiy_menu():
    print('1) Kirish')
    print('0) Chiqish')

def admin_menu(admin):
    while True:
        chiziq()
        print('ADMIN —', admin.ism)
        print('1 = Oqituvchi qoshish')
        print('2 = Oquvchi qoshish')
        print('3 = Guruh yaratish')
        print('4 = Guruhga oqituvchi biriktirish')
        print('5 = Guruhga oquvchi qoshish')
        print('6 = Royxatlar')
        print('0 = Chiqish')
        tan = input('Tanlang: ').strip()
        if tan == '1':
            login = input('Login: ').strip()
            parol = input('Parol: ').strip()
            ism = input('Ism familya: ').strip()
            t, xabar = markaz.oqituvchi_qosh(login, parol, ism)
            print(xabar)
        elif tan == '2':
            login = input('Login: ').strip()
            parol = input('Parol: ').strip()
            ism = input('Ism familya: ').strip()
            s, xabar = markaz.oquvchi_qosh(login, parol, ism)
            print(xabar)
        elif tan == '3':
            nomi = input('Guruh nomi: ').strip()
            kurs = input('Kurs tavsifi: ').strip()
            g, xabar = markaz.guruh_yarat(nomi, kurs)
            print(xabar, 'ID =', g.id)
        elif tan == '4':
            gid = input('Guruh ID: ').strip()
            tid = input('Oqituvchi ID: ').strip()
            if gid.isdigit() and tid.isdigit():
                print(markaz.guruhga_oqituvchi(int(gid), int(tid)))
            else:
                print('ID notogri.')
        elif tan == '5':
            gid = input('Guruh ID: ').strip()
            sid = input('Oquvchi ID: ').strip()
            if gid.isdigit() and sid.isdigit():
                print(markaz.guruhga_oquvchi(int(gid), int(sid)))
            else:
                print('ID notogri.')
        elif tan == '6':
            chiziq(); print('Oqituvchilar:')
            for t in markaz.ro_yxat_oqituvchilar():
                print(f"ID={t.id} | {t.ism} | login={t.login} | guruhlar={t.guruhlar}")
            chiziq(); print('Oquvchilar:')
            for s in markaz.ro_yxat_oquvchilar():
                print(f"ID={s.id} | {s.ism} | login={s.login} | guruh={s.guruh_id}")
            chiziq(); print('Guruhlar:')
            for g in markaz.ro_yxat_guruhlar():
                oq = markaz.oqituvchilar.get(g.oqituvchi_id)
                oq_ism = oq.ism if oq else '-'
                print(f"ID={g.id} | {g.nomi} | kurs={g.kurs} | oqituvchi={oq_ism} | oquvchilar={g.oquvchilar}")
        elif tan == '0':
            break
        else:
            print('Notogri tanlov.')

def oqituvchi_menu(oqituvchi):
    while True:
        chiziq()
        print('OQITUVCHI —', oqituvchi.ism)
        print('1) Mening guruhlarim')
        print('2) Baho qoyish')
        print('3) Guruhdagi baholarni korish')
        print('0) Chiqish')
        tan = input('Tanlang: ').strip()
        if tan == '1':
            gs = markaz.mening_guruhlarim(oqituvchi.id)
            if not gs:
                print('Guruh yoq.')
            else:
                for g in gs:
                    print(f"ID={g.id} | {g.nomi} | kurs={g.kurs} | oquvchilar={g.oquvchilar}")
        elif tan == '2':
            gid = input('Guruh ID: ').strip()
            sid = input('Oquvchi ID: ').strip()
            mavzu = input('Mavzu nomi: ').strip()
            ball_str = input('Ball (0-100): ').strip()
            if gid.isdigit() and sid.isdigit() and ball_str.isdigit():
                ball = int(ball_str)
                if ball < 0 or ball > 100:
                    print('Ball 0-100 oraligida bolishi kerak.')
                else:
                    print(markaz.baho_qoy(oqituvchi.id, int(gid), int(sid), mavzu, ball))
            else:
                print('Kiritishlarda xatolik.')
        elif tan == '3':
            gid = input('Guruh ID: ').strip()
            if not gid.isdigit():
                print('ID notogri.')
                continue
            g = markaz.guruhlar.get(int(gid))
            if not g or g.id not in oqituvchi.guruhlar:
                print('Guruh topilmadi yoki sizga tegishli emas.')
                continue
            for sid in g.oquvchilar:
                s = markaz.oquvchilar.get(sid)
                if not s:
                    continue
                print(f"{s.id}. {s.ism}")
                if not s.baholar:
                    print('  Baholar yoq')
                else:
                    for k in s.baholar:
                        print(' ', k, '->', s.baholar[k])
                print('  Ortacha:', markaz.oquvchi_ortacha(s.id))
        elif tan == '0':
            break
        else:
            print('Notogri tanlov.')

def oquvchi_menu(oquvchi):
    while True:
        chiziq()
        print('OQUVCHI —', oquvchi.ism)
        print('1) Guruhim')
        print('2) Baholarim')
        print('0) Chiqish')
        tan = input('Tanlang: ').strip()
        if tan == '1':
            if oquvchi.guruh_id is None:
                print('Siz hali birorta guruhga biriktirilmagansiz.')
            else:
                g = markaz.guruhlar.get(oquvchi.guruh_id)
                oq = markaz.oqituvchilar.get(g.oqituvchi_id) if g else None
                oq_ism = oq.ism if oq else '-'
                if g:
                    print(f"ID={g.id} | {g.nomi} | kurs={g.kurs} | oqituvchi={oq_ism}")
        elif tan == '2':
            if not oquvchi.baholar:
                print('Baholar yoq.')
            else:
                for k in oquvchi.baholar:
                    print(k, oquvchi.baholar[k])
                print('Ortacha:', markaz.oquvchi_ortacha(oquvchi.id))
        elif tan == '0':
            break
        else:
            print('Notogri tanlov.')

def boshlash():
    while True:
        chiziq(); print('Oquv markazi ')
        asosiy_menu()
        tan = input('Tanlang: ').strip()
        if tan == '1':
            login = input('Login: ').strip()
            parol = input('Parol: ').strip()
            foy = markaz.login_qil(login, parol)
            if not foy:
                print('Login yoki parol notogri.')
                continue
            if foy.rol == 'admin':
                admin_menu(foy)
            elif foy.rol == 'oqituvchi':
                oqituvchi_menu(foy)
            elif foy.rol == 'oquvchi':
                oquvchi_menu(foy)
            else:
                print('Rol notogri sozlangan.')
        elif tan == '0':
            print('Dastur tugadi.')
            break
        else:
            print('Notogri tanlov.')

if __name__ == '__main__':
    markaz = Markaz()
    boshlash()