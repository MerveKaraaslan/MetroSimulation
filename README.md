# Sürücüsüz Metro Simülasyonu: Rota Optimizasyonu Projesi
Bu proje, bir metro ağında iki istasyon arasında en az aktarmalı ve en hızlı rotaları hesaplamayı amaçlayan bir simülasyondur. Grafik teorisi ve arama algoritmaları kullanılarak, hayali bir metro ağı üzerinde rota optimizasyonu gerçekleştirilmiştir. Proje, gerçek dünya problemlerine algoritmik çözümler üretme becerisini geliştirmek için tasarlanmıştır.

## Kullanılan Teknolojiler ve Kütüphaneler
Proje aşağıdaki teknolojiler ve Python kütüphaneleri ile geliştirilmiştir:
- Python 3.10: Temel programlama dili olarak seçilmiştir. Nesne yönelimli programlama (OOP) desteği ve geniş kütüphane ekosistemi sayesinde metro ağı modellenmiş ve algoritmalar uygulanmıştır.
- collections.deque: BFS algoritmasında kuyruk yapısını oluşturmak için kullanılmıştır. Çift yönlü kuyruk (deque) yapısı, O(1) zamanında ekleme ve çıkarma işlemleri sunarak BFS’nin verimliliğini artırmaktadır.
- heapq: A* algoritmasında öncelik kuyruğu (priority queue) implementasyonu için tercih edilmiştir. Minimum yığın (min-heap) yapısı ile en düşük maliyetli rotanın hızlıca bulunması sağlanmıştır; logaritmik zaman karmaşıklığı (O(log n)) büyük ağlarda performans avantajı sunar.
- Nesne Yönelimli Programlama: Metro ağı, Istasyon ve MetroAgi sınıflarıyla modellenmiştir. Komşu istasyonlar bir sözlük (dict) yapısında tutularak graf yapısı etkin bir şekilde temsil edilmiştir.

## Algoritmaların Çalışma Mantığı
Proje, BFS ve A* algoritmalarını kullanarak rota optimizasyonu yapmaktadır. Aşağıda her algoritmanın işleyişi ve seçim nedenleri açıklanmıştır:
- BFS (Breadth-First Search) Algoritmasının Çalışma Mantığı: BFS, geniş öncelikli arama ile graf üzerinde katman katman ilerler. Başlangıç istasyonundan komşu istasyonları sırayla ziyaret eder ve hedefe ulaşıldığında en az adım (aktarma) içeren rotayı döndürür. collections.deque ile kuyruk yapısı oluşturulmuş, ziyaret edilen istasyonlar set ile takip edilerek döngüler önlenmiştir. Zaman karmaşıklığı O(V + E)’dir; burada V istasyon sayısı, E bağlantı sayısıdır.
- A* (A Star) Algoritmasının Çalışma Mantığı: A*, bilgiye dayalı bir arama algoritmasıdır ve toplam maliyeti (süre) minimize eder. Her adımda mevcut maliyet (g) ve heuristik tahmin (h) toplamı (f = g + h) hesaplanarak en düşük f değerine sahip rota öncelik kuyruğundan seçilir. Bu projede h=0 kabul edilerek Dijkstra benzeri bir davranış elde edilmiştir. heapq ile öncelik kuyruğu uygulanmış, minimum süreler bir sözlükte takip edilmiştir. Zaman karmaşıklığı O(E + V log V)’dir.
- Neden Bu Algoritmalar Kullanıldı: BFS, en az aktarmalı rotayı bulmak için uygundur çünkü graf üzerinde en kısa yol uzunluğunu (adım sayısı) garanti eder; bu, metro kullanıcıları için aktarma sayısını azaltma açısından önemlidir. A*, süre optimizasyonu için seçilmiştir; gerçek hayatta hız genellikle önceliklidir ve A*’ın heuristik yaklaşımı gereksiz yolları eleyerek verimlilik sağlar. Bu iki algoritma, farklı ihtiyaçlara (aktarma vs. süre) yönelik çözümler sunarak sistemin kapsamını genişletir.

## Örnek Kullanım ve Test Sonuçları

Aşağıdaki metro ağı oluşturulmuş ve algoritmalar test edilmiştir:

metro = MetroAgi()
metro.baglanti_ekle("A", "B", 10)
metro.baglanti_ekle("B", "C", 15)
metro.baglanti_ekle("A", "D", 20)
metro.baglanti_ekle("D", "E", 5)
metro.baglanti_ekle("E", "F", 8)
metro.baglanti_ekle("B", "F", 25)
metro.baglanti_ekle("F", "G", 7)
metro.baglanti_ekle("C", "H", 12)
metro.baglanti_ekle("G", "H", 10)

Test 1 - A -> H: En Az Aktarmalı Rota (BFS): ['A', 'B', 'C', 'H'] (3 adım, 2 aktarma); En Hızlı Rota (A*): ['A', 'B', 'C', 'H'], Süre: 37 dk (10+15+12). Alternatif rota (A-D-E-F-G-H = 50 dk) daha uzun olduğundan bu rota seçilmiştir.
Test 2 - B -> G: En Az Aktarmalı Rota (BFS): ['B', 'F', 'G'] (2 adım, 1 aktarma); En Hızlı Rota (A*): ['B', 'F', 'G'], Süre: 32 dk (25+7). Başka kısa yol bulunmamaktadır.
Test 3 - D -> C: En Az Aktarmalı Rota (BFS): ['D', 'A', 'B', 'C'] (3 adım, 2 aktarma); En Hızlı Rota (A*): ['D', 'A', 'B', 'C'], Süre: 45 dk (20+10+15). Alternatif rota mevcut değildir. Testler, algoritmaların doğruluğunu ve mantıklılığını doğrulamak için farklı senaryolarla denenmiştir.

## Projeyi Geliştirme Fikirleri
Projenin potansiyelini artırmak için aşağıdaki geliştirmeler planlanabilir:
- Görselleştirme: NetworkX ve Matplotlib ile metro ağının grafiksel temsili oluşturulabilir, böylece rotalar görsel olarak analiz edilebilir.
- Genişletilmiş Ağ: Mevcut 8 duraklı ağ, 20-30 duraklık bir sisteme genişletilerek algoritmaların büyük ölçekli performansı test edilebilir.
- Heuristik Optimizasyon: A* algoritmasına istasyonlar arası coğrafi mesafe bazlı bir heuristik eklenerek daha etkin bir arama sağlanabilir.
- Kullanıcı Arayüzü: Tkinter veya Flask ile bir arayüz geliştirilerek kullanıcıların rota sorgulaması yapması mümkün hale getirilebilir.
- Dinamik Süreler: Gerçek zamanlı yoğunluk simülasyonu için sürelerin değişken hale getirilmesi uygulanabilir.