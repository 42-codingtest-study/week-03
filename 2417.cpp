#include <bits/stdc++.h>//온갖 헤더 다때려박음
#include <iostream>
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c
void	ft_binary_search(long long n)
{
	long long start = 0, sqrtn = sqrt(n), end = sqrtn, mid;
	while (start <= end)
	{
		mid = (start + end) / 2;
		if (mid >= sqrtn)//루트값이랑 미드 같아질때까지
			end = mid - 1;
		else
			start = mid + 1;
	}
	 if(mid * mid == n)
		cout << mid;
	else
		cout << mid + 1;//외 않 됨????
}

int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	long long n;

	cin >> n;
	ft_binary_search(n);// 걍 sqrt(n)+ 1 출력하니 오버플로우일어남
}
