

class MyAccount {
    constructor(C_Num, C_Bal) {
        this.number = C_Num
        this.balance = C_Bal
    }

    deposit(amt) {
        let plus = this.balance + amt;
        return plus;
    }

    withdrow(amt) {
        let minus = this.balance - amt;
        return minus;
    }
}


class CheckingAccount extends MyAccount {
    constructor(date, dAmt, wAmt) {
        super(dAmt, wAmt)
        this.date = date
    }
    totalWithdrow() {
        return this.wAmt
    }
}


class SavingAccount {
    constructor(name, addr, dAmt, wAmt) {
        super(dAmt, wAmt)
        this.name = name
        this.address = addr
    }
    totaldePOSIT() {
        return this.wAmt
    }
}



let myAc = new MyAccount(8853289753, 2000)
let checkAc = new CheckingAccount(8853289753, 2000, 1000)
console.log('checkAc:', checkAc)
console.log('myAc:', myAc)
console.log('myD:', myAc.deposit(1000))
console.log('myD:', myAc.withdrow(500))