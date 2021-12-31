# Sort Challenge
Simple sort challenge based on the distance from a target value.

**CHALLENGE**<br>
INPUT:<br>
A sequence of int number <img src="https://latex.codecogs.com/svg.image?\left<&space;a_1,&space;a_2,&space;...&space;,&space;a_n&space;\right>" title="\left< a_1, a_2, ... , a_n \right>" /><br>
A target int number <img src="https://latex.codecogs.com/svg.image?k" title="k" />

OUTPUT:<br>
A sequence of int number <img src="https://latex.codecogs.com/svg.image?\left<&space;a_1,&space;a_2,&space;...&space;,&space;a_n&space;\right>" title="\left< a_1, a_2, ... , a_n \right>" /> that has this property: <img src="https://latex.codecogs.com/svg.image?\left|a_1-k&space;\right|&space;\leqslant&space;\left|a_2-k&space;\right|&space;\leqslant&space;...&space;\leqslant&space;\left|a_n-k&space;\right|" title="\left|a_1-k \right| \leqslant \left|a_2-k \right| \leqslant ... \leqslant \left|a_n-k \right|" />

<div align='center'>
  <img src="https://github.com/mariocuomo/sortChallenge/blob/main/challenge.png" width=700>
</div>

The critical step is the second. The total cost of the sort depends from the sorting algorithm used.
