const int BAUDRATE = 9600;
const int ENABLE_PIN = 12;
const int STEPS_PER_REV = 200;
const int STEP_DELAY = 2000;
String INPUT_BYTES;
String MOVES[30];
int NUM_MOVES = 0;

const int UPins[] = {2, 3}; //dir, step
const int RPins[] = {6, 7};
const int FPins[] = {8, 9};
const int DPins[] = {4, 5};
const int LPins[] = {10, 11};
const int BPins[] = {12, 13};

int dirStepPins[][2] = {
  {UPins[0], UPins[1]},
  {RPins[0], RPins[1]},
  {FPins[0], FPins[1]},
  {DPins[0], DPins[1]},
  {LPins[0], LPins[1]},
  {BPins[0], BPins[1]},
};

void turnMotor(int stepPin, int numSteps){
  for(int i = 0; i < numSteps; i++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(STEP_DELAY);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(STEP_DELAY);
  }
}

void makeMove(String moveString){
  char moveChar = moveString.charAt(0);
  int moveSteps = STEPS_PER_REV/4;
  int moveIndex = -1;
  switch(moveChar){
    case 'U':
      moveIndex = 0;
      break;
    case 'R':
      moveIndex = 1;
      break;
    case 'F':
      moveIndex = 2;
      break;
    case 'D':
      moveIndex = 3;
      break;
    case 'L':
      moveIndex = 4;
      break;
    case 'B':
      moveIndex = 5;
      break;
  }

  int moveDirPin = dirStepPins[moveIndex][0];
  int moveStepPin = dirStepPins[moveIndex][1];
  if (moveString.length() > 1 && moveString.charAt(1) == '\''){
    digitalWrite(moveDirPin, LOW);
  } else {
    digitalWrite(moveDirPin, HIGH);
  }
  
  if(moveString.length() > 1 && moveString.charAt(1) == '2'){ //rotate 180
    moveSteps *= 2;
  }

  turnMotor(moveStepPin, moveSteps);
}

int solve(String input){
  int prev = 0;
  int delimiter_index = input.indexOf(" ");
  while(delimiter_index > 0){
    MOVES[NUM_MOVES] = input.substring(prev, delimiter_index);
    NUM_MOVES += 1;
    delimiter_index = input.indexOf(" ", delimiter_index + 1);
  }
  for(int i = 0; i < NUM_MOVES; i++){
    makeMove(MOVES[i]);
  }
}

void setup() {
  Serial.begin(9600);
//  Serial.setTimeout(10);
  for(int i = 0; i < 6; i++){
    pinMode(dirStepPins[i][0],OUTPUT);
    pinMode(dirStepPins[i][1],OUTPUT);
  }
  
}

void loop() {
  //while(!Serial.available());
  //String INPUT_BYTES = Serial.readString();
  String INPUT_BYTES = "U D F' B2 U' D' L F U' D2 F' R2 U B2 R2 U D2 B2 L2 F2 D'";
  Serial.print(INPUT_BYTES);
  makeMove(INPUT_BYTES);
  while(1);
  
}
