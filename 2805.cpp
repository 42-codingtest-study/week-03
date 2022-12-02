//나무자르기

#include <bits/stdc++.h> //온갖 헤더 다때려박음

using namespace std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c

long long alltreelen(int mid, int n, int *arr) //집에 가져가는 나무의 길이
{
	long long res = 0;
	for (int i = 0; i < n; i++)
		if (arr[i] > mid)
			res += arr[i] - mid;
	return (res);
}

int main()
{
	ios_base::sync_with_stdio(0); // c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(0);					  // cin 전에 cout 버퍼 비우지 않게

	int n, m, start, end, mid;
	long long alllen;

	cin >> n >> m;
	int arr[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	end = *max_element(arr, arr + n); // maxelement == 각 자료형의 요소중 가장 큰값 주소 리턴 * 붙혀서 값 리턴
	start = 0;
	while (end > start)
	{
		mid = (end + start) / 2;
		alllen = alltreelen(mid, n, arr);
		if (alllen >= m && alltreelen(mid + 1, n, arr) < m) // 높이 최대라 자를 나무가 없을때
			break;
		else if (alllen < m) //나무 부족
			end = mid - 1;
		else if (alllen > m) //나무 충분
			start = mid + 1;
	}
	cout << (start + end) / 2;
}
