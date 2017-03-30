function fibonacci(index) {
  if (index < 2) {
    return index;
  }
  else {
    var sequence = [0, 1];
    for (x = 2; x <= index; x++) {
      sequence.push(sequence[x - 1] + sequence[x - 2]);
      console.log(sequence); // watching sequence array build each loop
    }
    return sequence[index];
  }
}
console.log(fibonacci(6));