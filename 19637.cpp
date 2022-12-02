//if문좀 대신 써줘
//하다가 너무 오류가 많고 도저히 해결될 각이 안보여서 풀이 참고했습니다
//vector 최고!

#include <bits/stdc++.h>//온갖 헤더 다때려박음
#include <iostream>

using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c
int	main()
{
	ios::sync_with_stdio(0);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(0); //cin 전에 cout 버퍼 비우지 않게

	int N, M;
	vector<int> vec;
	vector<string> vec_str;
	string str;
	int num;

	cin >> N >> M;
	int last_num = -1;
	for(int i = 1; i <= N; i++)
	{
		cin >> str >> num;
		if(num == last_num)
			continue;
		last_num = num;
		vec.push_back(num);
		vec_str.push_back(str);
	}
	for(int i = 1; i <= M; i++)
	{
		cin >> num;
		cout << vec_str[lower_bound(vec.begin(),vec.end(), num) - vec.begin()] << "\n";
	}//lowerbound (startaddr, endaddr, target) == targetidx
}

