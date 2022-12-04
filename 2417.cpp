//정수 제곱근
//sqrt함수 사용 시 오류 남
#include <bits/stdc++.h>//온갖 헤더 다때려박음
#include <iostream>
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c

int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	long long n, start, end, mid;

	cin >> n;
	start = 0;
	end = n;
	while (start <= end)
	{
		mid = (start + end) / 2;
		if (mid == 0 || mid == n / mid)// mid == 0일때 빼주기
			break;
		else if (mid > n / mid)
			end = mid - 1;
		else if (mid < n / mid)
			start = mid + 1;
	}
	if (mid * mid == n)
		cout << mid;
	else if (mid == 0 || mid == n / mid)
		cout << mid + 1;
	else
		cout << start;
}
