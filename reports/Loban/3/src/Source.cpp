#include "figure.h"

int main()
{
	Sphere sphere(3.4);
	sphere.Show();
	sphere.ShowVS();

	Sphere sphere2(5);
	sphere2.Show();
	sphere2.ShowVS();

	Sphere sphere3(3.4);
	sphere3.Show();
	sphere3.ShowVS();

	if (sphere == sphere2)
		cout << "sphere == sphere2" << endl;
	else
		cout << "sphere != sphere2" << endl;

	if (sphere != sphere3)
		cout << "sphere != sphere3" << endl;
	else
		cout << "sphere == sphere3" << endl;

	sphere = sphere2;

	if (sphere == sphere2)
		cout << "sphere == sphere2" << endl;
	else
		cout << "sphere != sphere2" << endl;
	
	Pyramid pyramid(20,8,20,60);
	pyramid.Show();
	pyramid.ShowVS();

	Cone cone(3,20, 28.2735, 60);
	cone.Show();
	cone.ShowVS();

	FiguresArray array;
	array.AddBack(&sphere);
	array.AddBack(&pyramid);
	array.AddBack(&cone);

	array.Show();

	try
	{
		cout << "Items" << endl;
		for(int i = 0; i < 5;i++)
			array[i]->Show();
	}
	catch(int i)
	{
		cout << "out of bounds" << endl;
	}
}