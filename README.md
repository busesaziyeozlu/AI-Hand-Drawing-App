# El Hareketi ile Çizim Uygulaması

Bu proje, gerçek zamanlı el hareketi algılama teknolojisi kullanarak kullanıcıların kamera aracılığıyla ekrana çizim yapmasını sağlayan bir bilgisayarlı görü uygulamasıdır.

## Proje Özeti

Uygulama, MediaPipe el landmark tespit modeli ve OpenCV kullanarak canlı kamera görüntüsü üzerinden el konumlarını analiz eder. Algılanan parmak durumlarına göre sistem farklı çizim modlarına geçiş yapar (renk seçimi, çizim, silme vb.).

Sistem, gerçek zamanlı görüntü işleme, landmark analizi ve sanal tuval (canvas) üzerine çizim işlemlerini birleştirerek etkileşimli bir kullanıcı deneyimi sunar.

## Özellikler

- İşaret parmağı ile çizim yapabilme
- Parmak kombinasyonlarına göre renk değiştirme
- El hareketi ile silgi moduna geçiş
- Gerçek zamanlı el takibi
- Canlı kamera etkileşimi

## Kullanılan Teknolojiler

- Python
- OpenCV
- MediaPipe
- NumPy

## Çalışma Mantığı

1. Kamera üzerinden canlı görüntü alınır.
2. Görüntü RGB formatına dönüştürülerek MediaPipe modeline gönderilir.
3. El landmark noktaları tespit edilir.
4. Parmak durumları landmark konumlarına göre analiz edilir.
5. Belirlenen moda göre sanal tuval üzerinde çizim veya silme işlemi gerçekleştirilir.
6. Tuval ile kamera görüntüsü birleştirilerek ekrana yansıtılır.
Uygulamadan çıkmak için `q` tuşuna basınız.
