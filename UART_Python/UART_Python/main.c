/*
 * UART_Python.c
 *
 * Created: 4/20/2021 1:58:19 AM
 * Author : hp
 */ 

#include "Display.h"
#include "DIO_Interface.h"

int main(void)
{
    /* Replace with your application code */
    Pin_Init(PINA1,INFREE);
	Display_Init();
	
	while (1) 
    {
		Display_Update();
    }
}

