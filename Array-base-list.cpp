#include<iostream>
using namespace std;

class ArrayList {

private:
	int *data;
	int length;
	int size;
	int *current;
	int *ncurrent;
	int *ptr_back;
	int *ptr_fwd;
	int *temp;
	int *temp_dup;
	int *temp2;
	int *ptr;
	int *ptr2;
	int *start;
	int *end;
	// put rest of the variable there

public:
	ArrayList(int size) {
		length = 0;
		current = 0;
		this->size = size;
		data = new int[size];
		current = data;
		
		for (int i=0; i<size; i++){
			*(data+i) = -1; 
		}
		
	}

	// Basic funtions. First implement these then add others funtion if you want
	void SimpleInsertion(int data) {
		if (length < size){
			*current = data;
			current++;
			length++;			
		}
		else{
			cout<<"List is full"<<endl;
		}

	}
	
	void InsertionAt(int value, int index) {
		int val_shifted;
		ncurrent = &(*(data + index));
		if(*ncurrent < 0)
			*ncurrent = value;
		else{
			if(length != size){ 
				ptr_fwd = (current-1); 
				ptr_back = (current-1);
				 
				for(int i=length-1; i>=index; i--){
					
					val_shifted = *ptr_fwd;
					ptr_fwd++;  
					*ptr_fwd = val_shifted;
					
					if(i!=index){
						ptr_back--;
						ptr_fwd = ptr_back;							
					}
					else{
						*ptr_back = value; 
					}
		
				}
				length++;
				current++;
			}
			else{
				cout<<"List is full already."<<endl;
			}

		}
	}

	void DeletionAt(int index) {
		temp = data;
		for(int i=0; i<length; i++){
			if( (i == index) ){
				if( (temp+1) != current){
					for(int j=i; j<=length; j++){ //from val's index to last element
						*temp = *(temp+1);				
						temp = temp + 1;
					}
				*temp = -1;
				current = current - 1;
				length = length - 1;
				return; 
				}
				else{
					*temp = -1;
					current = current - 1;
					length = length - 1;
					return;
				}
			}
			else{
				temp = temp + 1;
			}
		}
	}

	void DeleteData(int value) {
		temp = data;
		for(int i=0; i<length; i++){
			if ( (*temp == value) && ( (temp+1) != current) ) { 
				for(int j=i; j<=length; j++){ //from val's index to last element
					*temp = *(temp+1);				
					temp = temp + 1;
				}
				*temp = -1;
				current = current - 1;
				length = length - 1;
				return;
			}
			if ( (*temp == value) && ( (temp+1) == current) ){
				*temp = -1; 
				current = current - 1;
				length = length - 1;

				return;
			} 
			else{
				temp = temp + 1;
			}
		}
	}

	int find_index(int value) {
		temp = data;
		for(int i=0; i<length; i++){
			if(*temp == value){
				return i;
			}
			else
				temp = temp + 1;
		}
	}
	
	int find_value(int index){
		temp = data;
		for (int i=0; i<length; i++){
			if(i == index)
				return *temp;
			else
				temp = temp + 1;
		}
	}

	void emptyList() {
		temp = data;
		for(int i=0; i<=length; i++){
			*(temp+i) = -1;
		}
		cout<<"List is empty now"<<endl;
	}

	void copy(ArrayList obj) { 
		this->length = obj.length;
		this->size = obj.size;
		ptr = obj.data;
		ptr2 = this->data; //obj2
		for(int i=0; i<length; i++){ 
			*ptr2 = *ptr;
			ptr = ptr + 1;
			ptr2 = ptr2 + 1;
		}
	}

	void PrintList() {
		int *temp = data;
		for(int i=0; i<length; i++){
			cout<<*temp++<<" ";
		}
		cout<<endl;
	}
	
int main() {
 
	ArrayList obj1(4); //size must be accurate
	ArrayList obj2(5);
	ArrayList obj3(10);
	
	obj1.SimpleInsertion(1);
	obj1.SimpleInsertion(2);
	obj1.SimpleInsertion(3);
	obj1.SimpleInsertion(4); 
	
	obj2.SimpleInsertion(8);
	obj2.SimpleInsertion(7);
	obj2.SimpleInsertion(6);
	obj2.SimpleInsertion(2);
	obj2.SimpleInsertion(1); 	
	
//	obj2.copy(obj);
//	obj2.PrintList();
	
//	obj.InsertionAt(9, 3);
//	obj.PrintList();
//	obj.emptyList();

//	cout<<"Found at index: "<<obj.find_index(3)<<endl;
//	cout<<"Found value: "<<obj.find_value(2)<<endl;

//	obj.DeleteData(1); //val
//	obj.PrintList();
//	obj.DeleteData(5); //val
//	obj.PrintList();

//	obj.DeletionAt(4); //index
//	obj.PrintList();
//	obj.DeletionAt(0); //index
//	obj.PrintList();
