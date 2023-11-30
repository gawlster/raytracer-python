I created an object oriented model for my ray tracer.

I started by creating the vector class and defining all the methods I might need. For example, adding two vectors, adding a float or int to a vector, multiplying vectors, dividing vectors, etc. I created another class specifically for Color Vectors (called ColorVector), which extends the base vector class, but has a few extra goodies. For example, it adds r(), g(), and b() methods which return its values clamped between 0 and 255 instead of 0 and 1.

I created a class for the camera, which has one simple method which constructs the initial rays from the eye into the scene through the near plane.

I have a class for lights, which have a position vector and a light ColorVector. 

I have a class for spheres, which also have a position and color, along with a scale vector, ads coefficients (and specular exponent), and the near plane (this is used when calculating if intersections happen in the view port). This class has an intersection function, which takes in a ray, and optionally a light. It will calculate if the ray intersects the sphere, and return the hitPoint (in world coordinates), distance along the ray, and a boolean representing if the hit was inside the sphere or not. If the ray is a shadow ray, we also count intersections outside the viewport as valid. If there is any valid intersection, we return a hit (the actual vlues don't matter, only the fact that it was a hit). (The caveat here is that we need to check if the hit was closer than the light. If the light is closer, there is no hit). The sphere class also has a method to calculate the normal vector given a hitPoint in world coordinates.

The other main class is the ray class, which contains an origin and a direction (among a couple other things). It contains a trace function, which recursively casts rays until the MAX_RECURSION_DEPTH value, and accumulates the pixel color (ambient, diffuse, specular). It creates a shadow ray and casts toward each light. If there is no intersection, the color is used, else it is disregarded. It also constructs a reflection ray and recursively traces it, adding the returned color as the reflection color.

The only other main thing is the RayTracer class, which just reads the file and constructs the light objects and sphere obects. It basically is just the app controller.
