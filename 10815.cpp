#include <bits/stdc++.h>//온갖 헤더 다때려박음
#include <algorithm>
#include <iostream>// 입출력 가능하게 하는 헤더
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c

int	ft_binary_search(int arr[], int n, int m_num)
{
	int	mid, start = 0, end = n;
	while (1)
	{
		mid = ((start + end) / 2);
		if (arr[mid] == m_num)
			return (1);
		else if (arr[mid] < m_num)
			start = mid + 1;
		else if (arr[mid] > m_num)
			end = mid - 1;
		if (start > end)
			return (0);
	}
}

int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	int	n, m, m_num;
	cin >> n;
	int	arr[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr + n);// sort(배열, 배열의 주소+ len)
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> m_num;
		if (ft_binary_search(arr, n, m_num))
			cout << "1 ";
		else
			cout << "0 ";
	}
}
