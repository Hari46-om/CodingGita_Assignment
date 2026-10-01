# Assignment: Introduction to JavaScript
---

## Section A: Short Answer Questions (1 Mark each)

**Q1.** What is JavaScript?
```
Answer :
JavaScript is a high-level, dynamically typed programming language used to create interactive websites and applications.
```

**Q2.** Who created JavaScript and in which year?
```
Answer :
Created in 1995 by Brendan Eich at Netscape.
```

**Q3.** What was the original name of JavaScript?
```
Answer :
Originally named Mocha
```

**Q4.** Is JavaScript the same as Java? Give one major difference.
```
Answer :
Java is mainly a compiled, object-oriented language used for applications and backend systems, while JavaScript is primarily an interpreted/JIT language widely used to make websites interactive.
```

**Q5.** What does it mean when we say JavaScript is a **high-level** programming language?
```
Answer :
JavaScript uses simple, human-readable instructions.
```

**Q6.** Is JavaScript a compiled language or an interpreted language? Explain briefly.
```
Answer :
Modern JavaScript engines first compile the code into machine-level instructions using techniques such as Just-In-Time (JIT) compilation, then execute it. So, calling JavaScript simply “interpreted” is an oversimplification.
```

**Q7.** Name the JavaScript engines used by the following browsers:
- Google Chrome
- Mozilla Firefox
- Apple Safari
  
```
Answer :
- Google Chrome :- v8
- Mozilla Firefox :- SpiderMonkey
- Apple Safari :- 	JavaScriptCore
```
  

**Q8.** What is **Dynamic Typing** in JavaScript?
```
Answer :
In JavaScript, you do not need to declare the data type of a variable. JavaScript identifies the type while the program is running.
```

**Q9.** What is the main difference between a **static** website and a **dynamic** website?
```
Answer :
a static website shows the exact same prebuilt files to every visitor, while a dynamic website builds the page on-the-fly using databases and server-side code based on who is visiting or what they request
```

**Q10.** Name the three pillars of Front-end Web Development and write one line about each.
```
Answer :

- HTML :- Structure and Creates the content 
- CSS :- Style and Makes the content look good 
- JavaScript :- Behavior and Makes the content work 

```

**Q11.** What is the difference between Frontend and Backend?
```
Answer :
Front-end (also called client-side) development focuses on everything the user sees and interacts with in the browser.
Backend (also called server-side) development handles the logic, data processing, and storage that happen behind the scenes.
```

**Q12.** What is Node.js?
```
Answer :
Node.js is a runtime environment for JavaScript that allows JavaScript to run outside the browser.
```

**Q13.** Explain **ECMAScript**. What is its relation with JavaScript?
```
Answer :
ECMAScript is not a programming language like JavaScript. It is a standard or rulebook that defines how the JavaScript language should work.

JavaScript is a programming language that follows the ECMAScript standard. JavaScript engines use this standard to understand and execute JavaScript code. developer.mozilla

```

---

## Section B: True or False  
(Write True or False. If False, correct the statement)

1. JavaScript is a statically typed language.
```
Answer :-• False. JavaScript is a dynamically typed language.
```
2. JavaScript can only run inside the browser.
```
Answer :-False. JavaScript can run both inside and outside the browser (thanks to environments like Node.js).
```
3. HTML is responsible for the behaviour of a webpage.
```
Answer :-False. JavaScript is responsible for the behavior of a webpage, while HTML is responsible for its structure.
```
4. Node.js allows JavaScript to run outside the browser.
```
Answer :-True
```
5. JavaScript is case-insensitive.
```
Answer :-• False. JavaScript is case-sensitive.
```
6. `let name` and `let Name` are the same variable.
```
Answer :-• False. let name and let Name are different variables because JavaScript is case-sensitive.
```
7. ECMAScript is a programming language.
```
Answer :-• False. ECMAScript is a specification or standard, while JavaScript is the programming language that follows it.
```
8. React, Angular, and Vue.js are used for Backend development.
```
Answer :-1. False. React, Angular, and Vue.js are used for Frontend development.
```
---

## Section C: Fill in the Blanks

1. JavaScript was created by ______________ in the year ______________.
```
Answer :-Brendan Eich in 1995
```
2. The three technologies used in Front-end development are __________, __________, and __________.
```
Answer :-HTML , CSS and Javascript
```
3. JavaScript engines: Chrome uses __________, Firefox uses __________.
```
Answer :-v8 and SpiderMonkey
```
4. In the restaurant analogy: Customer = __________, Waiter = __________, Chef = __________.
```
Answer :- Customer =User ,Waiter =Server ,Chef =Database
```
5. JavaScript file extension is __________.
```
Answer :- .js
```
---

## Section D: Conceptual Questions (2 Marks each)

**Q14.** Differentiate between a **static website** and a **dynamic website**. Give one real-world example of each.
```
Answer :-Difference Between Static Website and Dynamic Website

Static Website:
A static website contains fixed content. The content is usually the same for every visitor and does not change unless the website developer manually updates the HTML files. Static websites are simple, fast, and easy to create.

Example: A school information website that only displays the school’s address, contact details, courses, and basic information.

Dynamic Website:
A dynamic website displays content that can change according to the user, time, or information stored in a database. Users can interact with the website, such as logging in, searching, commenting, or placing orders.

Example: Amazon is a dynamic website because it shows different products, prices, recommendations, and user information and allows users to search and place orders.

```

**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.
```
Answer :-
Two Features of JavaScript That Make It Suitable for Creating Interactive Web Pages

Event Handling:
JavaScript can respond to user actions such as clicking a button, moving the mouse, typing in a text box, or submitting a form. This makes web pages interactive.
Example: When a user clicks a button, JavaScript can display a message or change the content of the page.
DOM Manipulation:
JavaScript can change the content, style, and elements of a web page without reloading the entire page. It uses the Document Object Model (DOM) to access and modify HTML elements.
Example: JavaScript can change the text of a heading or change the background color when a user clicks a button.
```

**Q16.** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).
```
Answer :-Four Uses of JavaScript:

Server-side development – Node.js

Mobile app development – React Native

Desktop applications – Electron

Game development – Phaser
```

**Q17.** What is the difference between writing JavaScript code:
- Inside an HTML file using `<script>` tag, and
- In an external `.js` file?  
Mention two advantages of using an external JavaScript file.
```
Answer :-**Difference:**

* **Inside HTML using `<script>`:** JavaScript code is written directly in the HTML file.
* **External `.js` file:** JavaScript code is written in a separate file and linked to the HTML using `<script src="file.js"></script>`.

**Two advantages of external JavaScript:**

1. The same JavaScript file can be used on multiple HTML pages.
2. It makes the HTML code cleaner and easier to maintain.

```

**Q18.** Explain the difference between Frontend and Backend using the **restaurant analogy** in your own words.
```
Answer :-**Frontend:**
The frontend is like the **dining area of a restaurant**. It is what customers can see and interact with, such as tables, menus, and buttons.

**Backend:**
The backend is like the **kitchen of a restaurant**. Customers cannot see it, but it processes orders, prepares food, and manages everything behind the scenes.

**Example:** When you order food through a website, the **frontend** takes your order, while the **backend** processes it and sends the order to the kitchen.

```

**Q19.** Why should a beginner learn JavaScript? Write at least 4 points.
```
Answer :-

1. It is **easy to learn** for beginners.
2. It makes websites **interactive and dynamic**.
3. It is used in **web, mobile, desktop, and game development**.
4. It has a **large community and many learning resources**.
5. It provides **good career opportunities** in software development.

```
---

## Section E: Code-Based Questions (3 Marks each)

**Q20.** Predict the output of the following code and explain why:

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```

```
Answer :-**Output:**

```text
number
string
boolean
```

**Explanation:**

* `value = 25` → `25` is a **number**, so `typeof value` gives `number`.
* `value = "JavaScript"` → It is a **string**, so `typeof value` gives `string`.
* `value = false` → It is a **boolean**, so `typeof value` gives `boolean`.

JavaScript is **dynamically typed**, so the same variable can store different types of values.


**Q21.** Write a simple HTML + JavaScript program that displays an alert box with the message **"Welcome to JavaScript!"** when a button is clicked.
```
Answer :-

<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Alert</title>
</head>
<body>

    <button onclick="showMessage()">Click Me</button>

    <script>
        function showMessage() {
            alert("Welcome to JavaScript!");
        }
    </script>

</body>
</html>
```

**Q22.** Write JavaScript code to demonstrate **event-driven programming**.  
When a user clicks a button with id `"myBtn"`, the text of a paragraph with id `"demo"` should change to `"Button was clicked!"`.
```
Answer :-
<!DOCTYPE html>
<html>
<body>

    <button id="myBtn">Click Me</button>
    <p id="demo">Click the button.</p>

    <script>
        document.getElementById("myBtn").addEventListener("click", function() {
            document.getElementById("demo").textContent = "Button was clicked!";
        });
    </script>

</body>
</html>
```

---

## Section F: Practical / Application Based (5 Marks)

**Q23.** Create a complete web page (HTML + JavaScript) that includes the following:

1. A heading: **"My First JavaScript Page"**
2. A button labeled **"Click Me"**
3. When the button is clicked:
   - Show an alert: `"Hello, B.Tech Student!"`
   - Change the background color of the page to light blue
4. Also print `"JavaScript is running successfully!"` in the browser console.

**Write the complete code** (you can use Inline or External JavaScript).
```
Answer :-
<!DOCTYPE html>
<html>
<head>
    <title>My First JavaScript Page</title>
</head>
<body>

    <h1>My First JavaScript Page</h1>

    <button onclick="changePage()">Click Me</button>

    <script>
        console.log("JavaScript is running successfully!");

        function changePage() {
            alert("Hello, B.Tech Student!");
            document.body.style.backgroundColor = "lightblue";
        }
    </script>

</body>
</html>
```

---

## Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24.** JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML.  
In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of **Node.js** and **ECMAScript** updates in this growth.
```
Answer :-JavaScript became popular because it is **easy to learn, flexible, and supported by almost all web browsers**. It allows developers to make websites interactive and can also be used for many other types of applications.

1. **Node.js:** It allowed JavaScript to run outside the browser, especially on servers. This made JavaScript useful for **backend development** and APIs.

2. **ECMAScript Updates:** Regular ECMAScript updates introduced new features, making JavaScript more powerful, modern, and easier to use.

3. **Many Frameworks and Libraries:** Tools such as React, Angular, and Vue made JavaScript useful for building large and interactive applications.

4. **Wide Range of Uses:** JavaScript is now used for **frontend, backend, mobile apps, desktop apps, games, and AI/ML applications**.

Therefore, JavaScript grew from a browser scripting language into a **versatile programming language used across many areas of software development**.

```

---

