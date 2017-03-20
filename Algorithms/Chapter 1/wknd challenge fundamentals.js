var questions = [
'When it is a sunny cloudless day on earth, what color is the sky?',
'What is 2 + 2?',
'Have you ever paid $10,000 for a cheeseburger?',
'How many states are there in the United States of America?'
];

var responses = [];

var answers = [
'blue',
4,
'no',
50,
];

var questionsAnswered = 0;
var correctAnswers = 0;

var continueGame;

var person = prompt("Hi, what's your name?");
if (person !== '') {
}
else {
  console.log('Sorry, mind typing in your name for me?');
}

while (continueGame != 'Q') {
var accept = prompt("I'd like to ask you a few questions, would that be all right?"); 
if (accept == 'no') {
  break;
}
  
var startGame = prompt("If you'd like to stop at any point, just press 'Q'. Otherwise type 'go' to begin")
if (startGame == 'Q') {
  continueGame = startGame;
  console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
  break;
}

//  QUESTION 1
responses[0] = prompt('Great. ' + questions[0]);

if (responses[0] == 'Q') {
  continueGame = responses[0];
  console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
  break;
}
else if (responses[0] == answers[0]) {
  questionsAnswered++;
  correctAnswers++;
}
else {
  questionsAnswered++;
}

//  QUESTION 2
responses[1] = prompt(questions[1]);

if (responses[1] == 'Q') {
  continueGame = responses[1];
  console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
  break;
}
else if (responses[1] == answers[1]) {
  questionsAnswered++;
  correctAnswers++;
}
else {
  questionsAnswered++;
}

//  QUESTION 3
responses[2] = prompt(questions[2]);

if (responses[2] == 'Q') {
  continueGame = responses[2];
  console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
  break;
}
else if (responses[2] == answers[2]) {
  questionsAnswered++;
  correctAnswers++;
}
else {
  questionsAnswered++;
}

//  QUESTION 4
responses[3] = prompt(questions[3]);

if (responses[3] == 'Q') {
  continueGame = responses[3];
  console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
  break;
}
else if (responses[3] == answers[3]) {
  questionsAnswered++;
  correctAnswers++;
}
else {
  questionsAnswered++;
}

// End of Game
var endOfGame = prompt("Well done, thanks for playing along. Go ahead an hit 'Q' to see your results in the console");
console.log("Results for " + person + ":" + " you answered " + questionsAnswered + " questions," + " with " + correctAnswers + " correct answers" );
continueGame = endOfGame;
break;
}