import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.image as mpimg
import os
import winsound  # Windows alarm sesi için

# --- SİSTEM AYARLARI ---
anchors = np.array([[0, 0], [100, 0], [0, 100], [100, 100]])
safe_min, safe_max = 20, 80

def rssi_hesapla(mesafe):
    A, n = -40, 2
    if mesafe == 0: return A
    rssi = A - (10 * n * math.log10(mesafe))
    return rssi + np.random.normal(0, 2)

# --- ARKA PLAN HARİTASINI YÜKLE ---
harita_yolu = "mahalle.png" 
if os.path.exists(harita_yolu):
    arka_plan = mpimg.imread(harita_yolu)
else:
    arka_plan = None

# --- 1. MODELİ EĞİTME ---
X_train, y_train = [], []
for _ in range(500):
    x, y = np.random.uniform(0, 100), np.random.uniform(0, 100)
    sinyaller = [rssi_hesapla(np.linalg.norm(np.array([x,y]) - a)) for a in anchors]
    X_train.append(sinyaller)
    y_train.append([x, y])

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)

# --- 2. CANLI TAKİP EKRANI (PRO DASHBOARD) ---
plt.style.use('dark_background')
plt.ion()
fig, ax = plt.subplots(figsize=(10, 8))
fig.canvas.manager.set_window_title('WSN Geo-Fencing & Localization Dashboard')

cocuk_konum = np.array([50.0, 50.0])
rota_gercek = []

# Programın kapanıp kapanmadığını takip etmek için bayrak
is_running = True

def on_close(event):
    global is_running
    is_running = False

fig.canvas.mpl_connect('close_event', on_close)

for adim in range(100): # Daha uzun süre çalışması için adımı artırdım
    if not is_running:
        break
        
    # Çocuğun Hareketi
    cocuk_konum += np.random.uniform(-6, 6, size=2)
    cocuk_konum = np.clip(cocuk_konum, 0, 100)
    rota_gercek.append(cocuk_konum.copy())
    
    # Sinyal ve Tahmin
    su_anki_rssi = [rssi_hesapla(np.linalg.norm(cocuk_konum - a)) for a in anchors]
    tahmin = model.predict([su_anki_rssi])[0]
    
    ax.clear()
    
    if arka_plan is not None:
        ax.imshow(arka_plan, extent=[0, 100, 0, 100], aspect='auto')
        ax.add_patch(plt.Rectangle((0, 0), 100, 100, color='black', alpha=0.4))
    
    ax.add_patch(plt.Rectangle((safe_min, safe_min), 60, 60, edgecolor='lime', facecolor='lime', 
                               alpha=0.15, linewidth=2, linestyle='--', label='Güvenli Bölge'))
    
    
    
    rg = np.array(rota_gercek)
    ax.plot(rg[:,0], rg[:,1], color='cyan', linestyle='-', linewidth=2, alpha=0.7)
    
    ax.plot(cocuk_konum[0], cocuk_konum[1], marker='o', color='cyan', markersize=10, markeredgecolor='white', markeredgewidth=2)
    ax.plot(tahmin[0], tahmin[1], marker='+', color='red', markersize=20, markeredgewidth=3, label='Tahmin')
    ax.plot(tahmin[0], tahmin[1], marker='o', color='none', markeredgecolor='red', markersize=35, markeredgewidth=2, linestyle=':')
    
    # Durum Kontrolü ve ALARM SESİ
    if not (safe_min <= tahmin[0] <= safe_max and safe_min <= tahmin[1] <= safe_max):
        ax.set_title("[ ALARM ] HEDEF GÜVENLİ BÖLGEDE DEĞİL!", color='white', backgroundcolor='darkred', fontsize=16, fontweight='bold', pad=15)
        # 1000 Hz frekansında, 500 milisaniye (0.5 sn) süren alarm sesi
        winsound.Beep(1000, 500) 
    else:
        ax.set_title("[ SİSTEM AKTİF ] Hedef Takip Ediliyor", color='lime', fontsize=14, fontweight='bold', pad=15)
    
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_xticks([]); ax.set_yticks([]) 
    ax.legend(loc='lower right', facecolor='black', edgecolor='gray', labelcolor='white')
    
    plt.draw()
    plt.pause(1.0)

plt.ioff()
plt.close('all') # Program bittiğinde veya break olduğunda her şeyi kapat