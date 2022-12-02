//선분위의 점
//내장함수 최고

#include <bits/stdc++.h> //온갖 헤더 다때려박음
#include <iostream>
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c
int	main()
{
	ios::sync_with_stdio(0); //c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(0); //cin 전에 cout 버퍼 비우지 않게

	int n, m, start, end; //n == 점의개수 m == 선분의 개수

	cin >> n >> m;
	int	pointarr[n];
	for (int i = 0; i < n; i++)
		cin >> pointarr[i];
	sort(pointarr, pointarr + n);
	for (int i = 0; i < m; i++)
	{
		cin >> start >> end;
		cout << upper_bound(pointarr, pointarr + n, end) - lower_bound(pointarr, pointarr + n, start) << "\n";
	} //upperbound 타겟 초과 하는 값 인덱스 리턴 lowerbound 타겟 이랑 같거나 큰 처음 값 인덱스 리턴
}
