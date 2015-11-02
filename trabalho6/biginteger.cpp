#include "calculator.hpp"

using namespace std;

BigInteger::BigInteger() {
    this->signal = 1;
}

BigInteger::BigInteger(int i) {
    this->number.push_back(i);

    if (i < 0) {
        this->signal = -1;
    } else {
        this->signal = 1;
    }
}

BigInteger::BigInteger(vector<int> t) {
    this->number = t;
    this->signal = 1;
}

BigInteger::~BigInteger() {
}

bool BigInteger::isZero()
{
    for (int i = 0; i < (int) this->number.size(); i++)
    {
        if (this->number[i] != 0) {
            return false;
        }
    }

    return true;
}

void BigInteger::read()
{
    char c = '\0';
    int i = 0;
    this->number = vector<int>();

    while(cin.get(c))
    {
        if (c == '\n')
        {
            break;
        }

        if (c == '-') {
            this->signal = -1;
            i++;
            continue;
        }

        int num;
        istringstream ( string(1, c) ) >> num;

        this->number.push_back( num );
        i++;
    }

    this->clean();
}

void BigInteger::clean()
{
    if ((int) this->number.size() > 1 && this->number[0] == 0) {
        this->number.erase(this->number.begin(),this->number.begin()+1);
        this->clean();
    }
}

bool BigInteger::gte(BigInteger y)
{
    return this->compareTo(y) >= 0;
}

int BigInteger::compareTo(int y)
{
    BigInteger n = BigInteger(y);
    return this->compareTo(n);
}

int BigInteger::compareTo(BigInteger y)
{
    int xlen = (int) this->number.size();
    int ylen = (int) y.number.size();
    int sigx = this->signal;
    int sigy = y.signal;

    if (sigx != sigy) {
        if (this->isZero() && y.isZero()) {
            return 0;
        }

        if (sigx == -1) {
            // cout << "menor" << endl;
            return -1;
        } else {
            // cout << "maior" << endl;
            return 1;
        }
    }

    if (xlen != ylen) {
        return xlen > ylen ? 1 : -1;
    }

    for (int i = 0; i < xlen; i++)
    {
        // cout << "cmp " << this->number[i] << " " << y.number[i] << endl;
        if (this->number[i] > y.number[i]) {
            return 1;
        } else if (this->number[i] < y.number[i]) {
            return -1;
        }
    }

    return 0;
}

string BigInteger::toString()
{
    string s = "";

    if (this->signal == -1) {
        s += "-";
    }

    for (int i = 0; i < (int) this->number.size(); i++)
    {
        s += to_string(this->number[i]);
    }

    return s;
}

int BigInteger::atBackwards(int index)
{
    int n = (int) this->number.size() - 1;

    return this->number[n - index];
}

long int BigInteger::asLongInt()
{
    long int r;
    string str = this->toString();

    istringstream (str) >> r;

    return r;
}

void BigInteger::print()
{
    if (this->signal == -1) {
        cout << "-";
    }

    for (int i = 0; i < (int) this->number.size(); i++)
    {
        cout<<" "<<this->number[i];
    }
    cout<<endl;
}

BigInteger BigInteger::fromInt(int n)
{
    return BigInteger::fromLongInt(n);
}

BigInteger BigInteger::fromLongInt(long int n)
{
    std::string s = to_string(n);
    BigInteger r;

    if (n < 0) {
        r.signal = -1;
    } else {
        r.signal = 1;
    }

    for (int i = 0; i < s.length(); i++)
    {
        int num;
        istringstream ( string(1, s[i]) ) >> num;
        r.number.push_back(num);
    }

    return r;
}
