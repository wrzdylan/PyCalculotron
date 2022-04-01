const calculator = document.querySelector('.calculator')
const displayedNum = calculator.querySelector('.calculator__display')
const keys = calculator.querySelector('.calculator__keys')

keys.addEventListener('click', e => {
 if (e.target.matches('button')) {
    const key = e.target
    const action = key.dataset.action
    const previousKeyType = calculator.dataset.previousKeyType

    if (!action) {
        if (displayedNum === '0' || previousKeyType === 'operator') {
          display.textContent = keyContent
        } else {
          display.textContent = displayedNum + keyContent
        }
    }

    if (
        action === 'add' ||
        action === 'subtract' ||
        action === 'multiply' ||
        action === 'divide'
    ) {
        console.log('operator key!')
    }

    if (action === 'decimal') {
        console.log('decimal key!')
    }
      
    if (action === 'clear') {
        console.log('clear key!')
    }
      
    if (action === 'calculate') {
        console.log('equal key!')
    }
 }
})