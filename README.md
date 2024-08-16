# Web Scraping - Vatan Bilgisayar Ürün Verilerini Çekme

Bu proje, Vatan Bilgisayar web sitesinden ürün verilerini çekmek ve bir API aracılığıyla bir Microsoft SQL Server veritabanına kaydetmek için bir web scraping uygulamasıdır. Python, BeautifulSoup ve Requests kütüphanelerini kullanarak, ürün adı, marka, model numarası, fiyat, resim URL'si, kategori, derecelendirme ve derecelendirme sayısı gibi bilgileri toplar ve JSON formatında bir dosyaya kaydeder. Bu dosya daha sonra bir API aracılığıyla veritabanına aktarılabilir.

## Proje Amacı

Vatan Bilgisayar web sitesindeki ürünleri otomatik olarak izlemek ve verilerini bir veritabanında saklamak. Bu veriler, fiyat analizi, ürün karşılaştırması ve diğer analizler için kullanılabilir.

## Teknolojiler

* Python
* BeautifulSoup
* Requests
* JSON
* Microsoft SQL Server (API aracılığıyla)

## Proje Yapısı

1. **Kategorileri Belirleme:** Vatan Bilgisayar'da hangi kategorilerdeki ürünlerin bilgilerini çekeceğimizi belirliyoruz. Örneğin, "Bilgisayar", "Televizyon", "Telefon" gibi.
2. **Ürünleri Tarama:** Belirlediğimiz kategorilerdeki her ürün sayfasını tek tek ziyaret ederiz.
3. **Bilgileri Çekme:** Her ürün sayfasından ürünün adını, fiyatını, resmini, markasını, modelini ve diğer bilgilerini alırız.
4. **Kategori Oluşturma (Gerekirse):** Eğer ürünün kategorisi veritabanımızda yoksa, yeni bir kategori oluştururuz.
5. **Veritabanına Kaydetme:** Çektiğimiz bilgileri ve kategori bilgilerini bir API aracılığıyla veritabanımıza göndeririz.

## API Entegrasyonu

Proje, `API_BASE_URL` değişkeninde belirtilen bir API ile entegre olur. `get_category_id()` ve `create_category()` fonksiyonları, API ile iletişim kurarak kategori bilgilerini alır ve yeni kategoriler oluşturur. Bu API, verileri Microsoft SQL Server veritabanına kaydetmek için kullanılır.

## Kullanım

1. **Gerekli kütüphaneleri yükleyin:**
    ```dash
    pip install requests beautifulsoup4 urllib3

3. **`API_BASE_URL` değişkenini API'nizin URL'si ile güncelleyin.**
4. **Scripti çalıştırın:**
    ```dash
    python main.py
   
6. **Script, Vatan Bilgisayar web sitesinden ürünleri çeker ve `request.json` dosyasına kaydeder.**
7. **`request.json` dosyasını API'nize göndererek verileri veritabanına kaydedebilirsiniz.**

## Önemli Notlar

* Bu script, Vatan Bilgisayar web sitesinin yapısına bağlıdır. Web sitesi yapısında değişiklik olursa, scriptin güncellenmesi gerekebilir.
* Web scraping yaparken, web sitesinin kullanım koşullarına uymak önemlidir.
* Bu proje, [.NET E-Commerce API](https://github.com/mevlutayilmaz/e-commerce-api) ile entegre çalışacak şekilde tasarlanmıştır.

## Sonuç

Bu proje, Vatan Bilgisayar web sitesinden ürün verilerini çekmek ve bir veritabanına kaydetmek için basit ve etkili bir yöntem sunar. Proje, web scraping ve API entegrasyonu konularında öğrenmek ve geliştirmek için iyi bir başlangıç noktasıdır.
