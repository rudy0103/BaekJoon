#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <fstream>
using namespace std;

string input;
int match_front_back[200]; //[앞 괄호의 인덱스] = 매치되는 뒷 괄호의 인덱스
vector<string> result;

void Solve(int index, vector<int> select)
{
	if (index == input.size())
	{
		string maked = "";

		for (int i = 0; i < input.size(); i++)
		{
			if (input[i] == '(' || input[i] == ')')
			{
				if (select[i] == 1) //선택한 괄호 일때
					maked += input[i];

				else
					continue;
			}

			else
				maked += input[i];
		}

		//input값이랑 같다면 괄호 쌍을 제거하지 않은것이므로
		if (input != maked)
			result.push_back(maked);

		return;
	}

	if (input[index] == '(')
	{
		//해당 괄호를 포함하지 않을때
		Solve(index + 1, select);

		//해당 괄호를 포함할때
		select[index] = 1;
		select[match_front_back[index]] = 1;
		Solve(index + 1, select);
	}

	else
		Solve(index + 1, select);
}

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
    // freopen("input.txt","rt",stdin);
	cin >> input;

	stack<int> s;
	for (int i = 0; i < input.size(); i++)
	{
		if (input[i] == '(')
			s.push(i);

		else if (input[i] == ')')
		{
			int match_front = s.top();

			match_front_back[match_front] = i; //매치되는 인덱스를 저장한다

			s.pop();
		}
	}

	vector<int> select(input.size(), 0);
	Solve(0, select);

	ofstream writeFile;
	writeFile.open("output.txt");


	sort(result.begin(), result.end());
	result.erase(unique(result.begin(), result.end()), result.end()); //같은 문자열 제거
	int cnt=0;
	for (int i = 0; i < result.size(); i++){
		cout << result[i] << "\n";
		cnt++;
		if(writeFile.is_open()){
			result[i]+='\n';
			writeFile.write(result[i].c_str(),result[i].size());
		}
	}
	// cout<<cnt;
	writeFile.close();


	return 0;
}