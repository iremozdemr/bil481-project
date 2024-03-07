import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.json.JSONArray;
import org.json.JSONObject;

public class API_tut {
    public static void main(String[] args) {
        try {
            // API endpoint URL
            URL url = new URL("https://api.adsb.lol/v2/pia");

            // HTTP GET isteği oluşturma
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            // Yanıtı okuma
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String inputLine;
            while ((inputLine = reader.readLine()) != null) {
                response.append(inputLine);
            }
            reader.close();

            // JSON olarak yanıtı işleme
            JSONObject jsonObject = new JSONObject(response.toString());

            // "ac" anahtarından uçaklar dizisini alma
            JSONArray aircrafts = jsonObject.getJSONArray("ac");

            // Her bir uçak için bilgileri alma ve yazdırma
            // for döngüsü içinde yapılan işlemler örnek teşkil etmektedir
            for (int i = 0; i < aircrafts.length(); i++) {
                JSONObject aircraft = aircrafts.getJSONObject(i);
                String flight = aircraft.getString("flight");
                double lat = aircraft.getDouble("lat");
                double lon = aircraft.getDouble("lon");
                int alt = aircraft.getInt("alt_geom");
                System.out.println("Uçuş: " + flight + ", Enlem: " + lat + ", Boylam: " + lon + ", Yükseklik: " + alt);
            }

            // Bağlantıyı kapatma
            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}