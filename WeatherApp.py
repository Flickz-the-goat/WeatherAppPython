import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt 

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter city name: ", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButt = QPushButton("Get Weather", self)
        self.tempLabel = QLabel(self)
        self.emojiLabel = QLabel( self)
        self.desLabel = QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherButt)
        vbox.addWidget(self.tempLabel)
        vbox.addWidget(self.emojiLabel)
        vbox.addWidget(self.desLabel)
        
        self.setLayout(vbox)
        
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.tempLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.emojiLabel.setAlignment(Qt.AlignCenter)
        self.desLabel.setAlignment(Qt.AlignCenter)
        
        self.cityLabel.setObjectName("cityLabel")
        self.tempLabel.setObjectName("tempLabel")
        self.cityInput.setObjectName("cityInput")
        self.emojiLabel.setObjectName("emojiLabel")
        self.desLabel.setObjectName("desLabel")
        self.getWeatherButt.setObjectName("getWeatherButt")
        
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#cityLabel{
                font-size: 40px;
                font-style: italic;
            }   
            QLineEdit#cityInput{
                font-size: 40px;
                
            }   
            QPushButton#getWeatherButt{
                font-size: 30px;
                font-weight: bold;
            }  
            QLabel#tempLabel{
                font-size: 75px;
                
            }
            QLabel#emojiLabel{
                font-size: 90px;
                font-family: Segoe UI emoji;
            }
            QLabel#desLabel{
                font-size: 50px;
            }
         """)
        
        self.getWeatherButt.clicked.connect(self.getWeather)

    def getWeather(self):
        apiKey = "TV7E42S4R7HDN8C66NC6ZVTQT"
        city = self.cityInput.text()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={apiKey}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        self.displayWeather(data)
        
    def displayWeather(self, data):
        temp = data["currentConditions"]["temp"]
        des = data["description"]
        condition = data["currentConditions"]["conditions"]
        self.tempLabel.setText(f"{temp}")
        self.desLabel.setText(f"{des}")
        print(condition)
        match condition:
            case "Partially cloudy":
                self.emojiLabel.setText('⛅')
            case "Sunny":
                self.emojiLabel.setText('☀️')
            case "Cloudy":
                self.emojiLabel.setText('☁️')
            case "Rain, Partially cloudy":
                self.emojiLabel.setText('🌧️')
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())