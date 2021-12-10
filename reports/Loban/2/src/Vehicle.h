#ifndef VEHICLE_H
#define VEHICLE_H

class Vehicle
{
protected:
	int speed;
public:
	static Vehicle** items;
	static int count;
	Vehicle();
	Vehicle(int speed, bool isAdd );
	Vehicle(Vehicle& vehicle);
	~Vehicle();
    static void ShowItems();
	virtual void AddItem() final;
	virtual void Show() = 0;
};

class Auto : public Vehicle
{
protected:
	const char* marka;
public:
	Auto();
	Auto(int speed, const char* marka, bool isAdd);
	Auto(Auto& _auto);
	~Auto();
    void Show() override;
};

class Train : public Vehicle
{
protected:
	const char* direction;
public:
	Train();
	Train(int speed, const char* direction, bool isAdd);
	Train(Train& train);
	~Train();
	void Show() override;

};

class Express : public Train
{
	int maxSpeed;
public:
	Express();
	Express(int speed, const char* direction, int maxSpeed, bool isAdd);
	Express(Express& express);
	~Express();
	void Show() override;
};

#endif //VEHICLE_H
