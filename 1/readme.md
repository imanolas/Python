Description:
In the two-dimensional space we have two vectors a and b starting with the point (0,0) of the axes and finally the points with Cartesian coordinates a1, a2 and b1, b2 respectively (on the x and y axes as shown in the figure).

![1](https://user-images.githubusercontent.com/73962468/103141556-94fa4800-46fe-11eb-9cef-955d401157b2.jpg)

The angle θ formed by the two vectors with each other has a cosine given by the formula: 

![2](https://user-images.githubusercontent.com/73962468/103141592-341f3f80-46ff-11eb-9290-6a1063fc6c6e.jpg)
 
Where:

![3](https://user-images.githubusercontent.com/73962468/103141605-4d27f080-46ff-11eb-9a8c-160508ae1c27.jpg)

![4](https://user-images.githubusercontent.com/73962468/103141606-4dc08700-46ff-11eb-9d21-2ca022fcdaf1.jpg)

![5](https://user-images.githubusercontent.com/73962468/103141607-4f8a4a80-46ff-11eb-8425-f66a421ffcb9.jpg)

   
Write a program that reads from the keyboard the values of a1, a2 and b1, b2 and calculates the cosine of the angle θ (name the costh) and the angle θ in degrees (name the goniath). Your program displays costh & goniath values on the screen 

ATTENTION TO THE NAMES 

DEFINITELY use the following names otherwise your password will not be rated:

a1, a2 and b1, b2 for the coordinates of the vectors a and b as shown in the figure
costh for the cosine of the angle θ
goniath for the angle θ 

SUGGESTIONS

Remember and use the math library
We assume that the user always enters numeric values (whole or real) and your password does not need to do any additional checking.
We also consider that the user gives values to a1, a2 & b1, b2 non-zero so that there is no division by zero in the denominator in the cosine type. So you do not need to do anything about it.
Note that a.b does NOT mean "a over b" multiplication. It is simply a symbol of the inner product of vectors. You can easily calculate it from the formula we give.
Also note that in the denominator of the formula for the cosine we have the product of the measures of the vectors, i.e. | a | on | b |, where the measures will be calculated from the formulas we give you.
Finally note that we ask for the angle θ in degrees (not radii). Look at the information in the math library. 
