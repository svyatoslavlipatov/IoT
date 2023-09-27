# LedMatrix

## Заполненная таблица

<center>
| leds | D7 | D8 | D11 | D12 |
| --- | --- | --- | --- | --- |
| 1 | H  | L  | L | H |
| 2 | H | L | H | L |
| 3 | L | H | L | H |
| 4 | L | H | H | L |
| 1, 2 | H | L | L | L |
| 3, 4 | L | H | L | L |
| 1, 3 | H | H | L | H |
| 2, 4 | H | H | H | L |
| 1,4 | switch 1/4 |  |  |  |
| 2, 3 | switch 2/3 |  |  |  |
| 1, 2, 3 | switch 1, 2/3 |  |  |  |
| 2, 3, 4 | switch 2/3, 4 |  |  |  |
| 3, 4, 1 | switch 1/3, 4 |  |  |  |
| 4, 1, 2 | switch 1, 2/4 |  |  |  |
| 1, 2, 3, 4 | H | H | L | L |
| ни одного | L | L | L | L |
</center>

## Код

```cpp
const int PIN_7 = 7;
const int PIN_8 = 8;
const int PIN_11 = 11;
const int PIN_12 = 12;

int easy_combinations[][4] = {
  {HIGH, LOW, LOW, HIGH}, // 1
  {HIGH, LOW, HIGH, LOW}, // 2
  {LOW, HIGH, LOW, HIGH}, // 3
  {LOW, HIGH, HIGH, LOW}, // 4
  {HIGH, LOW, LOW, LOW}, // 1,2
  {LOW, HIGH, LOW, LOW}, // 3,4
  {HIGH, HIGH, LOW, HIGH}, // 1,3
  {HIGH, HIGH, HIGH, LOW},  // 2,4
  {HIGH, HIGH, LOW, LOW}, // 1,2,3,4
  {LOW, LOW, LOW, LOW} // nothing
};

int switch_combinations[][2][4] = {
  {{HIGH, LOW, LOW, HIGH}, {LOW, HIGH, HIGH, LOW}}, // 1,4
  {{HIGH, LOW, HIGH, LOW}, {LOW, HIGH, LOW, HIGH}}, // 2,3
  {{HIGH, LOW, LOW, LOW}, {LOW, HIGH, LOW, HIGH}}, // 1,2,3
  {{HIGH, LOW, HIGH, LOW}, {LOW, HIGH, LOW, LOW}}, // 2,3,4
  {{HIGH, LOW, LOW, HIGH}, {LOW, HIGH, LOW, LOW}}, // 3,4,1
  {{HIGH, LOW, LOW, LOW}, {LOW, HIGH, HIGH, LOW}}, // 4,1,2
};

void setup() {
  pinMode(PIN_7, OUTPUT);
  pinMode(PIN_8, OUTPUT);
  pinMode(PIN_11, OUTPUT);
  pinMode(PIN_12, OUTPUT);
}

void stop() {
  digitalWrite(PIN_7, LOW);
  digitalWrite(PIN_8, LOW);
  digitalWrite(PIN_11, HIGH);
  digitalWrite(PIN_12, HIGH);
}

void loop() {
  for (int i = 0; i < 8; i++) {  
    stop();
    digitalWrite(PIN_7, easy_combinations[i][0]);
    digitalWrite(PIN_8, easy_combinations[i][1]);
    digitalWrite(PIN_11, easy_combinations[i][2]);
    digitalWrite(PIN_12, easy_combinations[i][3]);
    delay(1550);
  }
  
  for (int i = 0; i < 6; i++) {  
    for (int j = 0; j < 700; j++) {
      stop(); 
      digitalWrite(PIN_7, switch_combinations[i][0][0]);
      digitalWrite(PIN_8, switch_combinations[i][0][1]);
      digitalWrite(PIN_11, switch_combinations[i][0][2]);
      digitalWrite(PIN_12, switch_combinations[i][0][3]);
      delay(1);
      stop();
      digitalWrite(PIN_7, switch_combinations[i][1][0]);
      digitalWrite(PIN_8, switch_combinations[i][1][1]);
      digitalWrite(PIN_11, switch_combinations[i][1][2]);
      digitalWrite(PIN_12, switch_combinations[i][1][3]);
      delay(1);
      stop();
    }
  }
  
  for (int i = 8; i < 10; i++) {  
    stop();
    digitalWrite(PIN_7, easy_combinations[i][0]);
    digitalWrite(PIN_8, easy_combinations[i][1]);
    digitalWrite(PIN_11, easy_combinations[i][2]);
    digitalWrite(PIN_12, easy_combinations[i][3]);
    delay(1550);
  }
  
}
```

## Демонстрация работы
https://github.com/svyatoslavlipatov/IoT/assets/92099105/3021a7b0-5825-4446-b091-013a394ee1b7
