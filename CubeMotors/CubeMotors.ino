const int BAUDRATE = 9600;
const int STEPS_PER_REV = 200;
const int STEP_DELAY = 1200;
String INPUT_BYTES;

const int UPins[] = {2, 3}; //dir, step
const int RPins[] = {6, 7};
const int FPins[] = {42, 43};
const int DPins[] = {4, 5};
const int LPins[] = {4, 5};
const int BPins[] = {52, 53};

int dirStepPins[][2] = {
  {UPins[0], UPins[1]},
  {DPins[0], DPins[1]},
  {LPins[0], LPins[1]},
  {RPins[0], RPins[1]},
  {FPins[0], FPins[1]},
  {BPins[0], BPins[1]},
};

//Ex: "R L U2 R L' B2 U2 R2 F2 L2 D2 L2 F2"
void moveMotor(String moveString){ //X or X' or X2
  char moveChar = moveString.charAt(0);
  int movePins[2];
  int moveSteps = STEPS_PER_REV/4;
  int moveIndex = -1;
  switch(moveChar){
    case 'U':
      moveIndex = 0;
      break;
    case 'D':
      moveIndex = 1;
      break;
    case 'L':
      moveIndex = 2;
      break;
    case 'R':
      moveIndex = 3;
      break;
    case 'F':
      moveIndex = 4;
      break;
    case 'B':
      moveIndex = 5;
      break;
   }
   movePins[0] = dirStepPins[0][moveIndex];
   movePins[1] = dirStepPins[1][moveIndex];
  
  if(moveString.length() > 1 && moveString.charAt(1) == '\''){ //counterclockwise
    digitalWrite(movePins[0], LOW);
  } else{                                                     //clockwise
    digitalWrite(movePins[0], HIGH);
  }
  
  if(moveString.length() > 1 && moveString.charAt(1) == '2'){ //rotate 180
    moveSteps *= 2;
  }
  
  for(int i = 0; i < moveSteps; i++){
    digitalWrite(movePins[1], HIGH);
    delayMicroseconds(STEP_DELAY);
    digitalWrite(movePins[1], LOW);
    delayMicroseconds(STEP_DELAY);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUDRATE);
  for(int i = 0; i < 6; i++){
    pinMode(dirStepPins[i][0],OUTPUT);
    pinMode(dirStepPins[i][1],OUTPUT);
  }

}

void loop() {
//  // put your main code here, to run repeatedly:
//  if(Serial.available() > 0){
//    INPUT_BYTES = Serial.readStringUntil('\n');
//    Serial.print(INPUT_BYTES);
//  }
//  String bufferStr = "";
//  for(int i = 0; i < INPUT_BYTES.length(); i++){
//    if(INPUT_BYTES[i] != ' '){
//      bufferStr += INPUT_BYTES[i];
//    } else if (bufferStr != ""){
//      moveMotor(bufferStr);
//                          //testing
//      bufferStr += '\n';
//      for(int i = 0; i < bufferStr.length(); i++){
//        Serial.write(bufferStr[i]);
//      }
//      Serial.write('\n');
//                          //testing
//      bufferStr = "";
//    }
//  }
  for(int i = 0; i < 50; i++){
    digitalWrite(3, HIGH);
    delayMicroseconds(STEP_DELAY);
    digitalWrite(3, LOW);
    delayMicroseconds(STEP_DELAY);
  }
  for(int i = 0; i < 50; i++){
    digitalWrite(5, HIGH);
    delayMicroseconds(STEP_DELAY);
    digitalWrite(5, LOW);
    delayMicroseconds(STEP_DELAY);
  }
  
}
