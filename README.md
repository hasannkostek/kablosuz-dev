# Kablosuz Sensör Ağları Coğrafi Sınırlandırma ve Konumlandırma Kontrol Paneli 📡🤖

## 🎓 Proje Hakkında ve Teşekkür
Bu proje, **Dr. Öğr. Üyesi Hasan Serdar** hocamızın değerli danışmanlığında ve yönlendirmeleriyle, **Kablosuz Algılayıcı Ağlar** dersi kapsamında geliştirilmiştir. Süreç boyunca sunduğu akademik vizyon ve destekleri için kendisine teşekkür ederim.

## 🚀 Proje Özeti
Bu sistem, GPS sinyallerinin yetersiz, verimsiz veya yüksek maliyetli olduğu alanlarda, düşük maliyetli sensörlerden alınan **RSSI** verilerini kullanarak gerçek zamanlı konum tespiti yapar. Klasik matematiksel yöntemlerdeki gürültü hatalarını aşmak için **KKNN** makine öğrenmesi algoritması kullanılmıştır.

Projenin konsept senaryosu **"Güvenli Mahalle ve Çocuk Takibi"** üzerine kurgulanmıştır. Sistem, belirlenen güvenli oyun alanının dışına çıkılması durumunda hem görsel hem de işitsel alarm üreten, otonom ve interaktif bir radar paneline sahiptir.

## 🛠️ Teknik Özellikler ve Metrikler
* **Log-Distance Path Loss Modeli:** Gerçek dünya sinyal sönümlenmesi ve Gaussian gürültüsü matematiksel olarak simüle edilmiştir.
* **Yapay Zeka (KNN) Regresyonu:** Sinyal dalgalanmalarını filtreleyerek anlık, yüksek doğruluklu ve düşük gecikmeli konum kestirimi.
* **Gerçek Zamanlı Radar Arayüzü:** Matplotlib tabanlı, profesyonel "Dark Mode" endüstriyel arayüz ile anlık hedef takibi.
* **Dinamik Geo-Fencing:** Hedef, sanal çit sınırlarını ihlal ettiğinde anında tetiklenen görsel uyarılar ve sesli ikaz sistemi.

## 📂 Dosya Yapısı
* `mahalle_bekcisi.py`: Modelin eğitildiği ve canlı izleme panelinin çalıştığı ana kaynak kod.
* `mahalle.png`: Radar ekranının arka planında kullanılan harita referansı.
* `requirements.txt`: Sistemin çalışması için gereken Python bağımlılıkları.
