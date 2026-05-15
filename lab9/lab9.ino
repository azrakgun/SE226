
const int LED1 = 43, LED2 = 44, LED3 = 45, LED4 = 46;
const int btn1Pin = 38, btn2Pin = 39;

// Değişkenler
bool systemOn = false;    
int currentMode = 1;     
bool lastBtn1 = LOW, lastBtn2 = LOW; 

unsigned long prevTime = 0; 
int ledStep = 0;         
void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT); pinMode(LED4, OUTPUT);
  pinMode(btn1Pin, INPUT); pinMode(btn2Pin, INPUT);
}

void loop() {
  
  bool btn1 = digitalRead(btn1Pin);
  bool btn2 = digitalRead(btn2Pin);

  
  if (btn1 == HIGH && lastBtn1 == LOW) {
    systemOn = !systemOn;
    if (!systemOn) allOff();
    delay(50); 
  }
  lastBtn1 = btn1;

  
  if (systemOn && btn2 == HIGH && lastBtn2 == LOW) {
    currentMode++;
    if (currentMode > 3) currentMode = 1;
    ledStep = 0; 
    allOff();   
    delay(50); 
  }
  lastBtn2 = btn2;

  if (systemOn) {
    unsigned long now = millis();
    if (now - prevTime >= 1000) { // 1 saniye dolunca bir sonraki adıma geç
      prevTime = now;
      runSelectedMode();
    }
  }
}

void runSelectedMode() {
  allOff();
  switch (currentMode) {
    case 1: 
      static bool toggle = false;
      toggle = !toggle;
      if (toggle) {
        digitalWrite(LED1, HIGH); digitalWrite(LED2, HIGH);
        digitalWrite(LED3, HIGH); digitalWrite(LED4, HIGH);
      }
      break;

    case 2: 
      digitalWrite(43 + ledStep, HIGH);
      ledStep = (ledStep + 1) % 4;
      break;

    case 3: 
      digitalWrite(46 - ledStep, HIGH);
      ledStep = (ledStep + 1) % 4;
      break;
  }
}

void allOff() {
  digitalWrite(LED1, LOW); digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW); digitalWrite(LED4, LOW);
}