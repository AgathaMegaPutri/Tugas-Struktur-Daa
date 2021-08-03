class GameEntry:
    total_player = 0

    def __init__(self, nama, skor, waktu):
        self.nama = nama
        self.skor = skor
        self.waktu = waktu
        
        GameEntry.total_player += 1
    
    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setSkor(self, skor):
        self.skor = skor
    
    def getSkor(self):
        return self.skor

    def setWaktu(self, waktu):
        self.waktu = waktu

    def getWaktu(self):
        return self.waktu

    def getTotal():
        return GameEntry.total_player

class ScoreBoard:

    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.board = [None] * self.kapasitas
        self.n = 0 
    
    def getCapacity(self):
        return self.kapasitas

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        skor = entry.getSkor()

        condition = len(self.board) > self.n or skor > self.board[self.kapasitas - 1].getSkor()
        # print(condition)

        if condition:
            if self.n < self.kapasitas:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].getSkor() < skor:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"Entri {skor} ditambahkan!")

    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'nama'), getattr(self.board[i], 'skor'))

board = ScoreBoard(10)


active = True

while active:
    print("")
    start = input("Opsi: \n 1 = Menambahkan Entry Baru \n 2 = Menampilkan List Dari ScoreBoard \n 3 = Keluar \n")
    print("")
    if start == '2':
        board.listEntries()
    elif start == '1':
        nama = input("Masukkan nama pemain ")
        skor = int(input("Masukkan skor "))
        waktu = int(input("Masukkan waktu "))

        in_skor = GameEntry(nama, skor, waktu)
        set_board = board.addItem(in_skor)

        print(f"Entri baru ditambahkan: {in_skor.getNama()} {in_skor.getSkor()} {in_skor.getWaktu()}")
    else:
        break
