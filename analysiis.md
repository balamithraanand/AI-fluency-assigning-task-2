# Day 2 – Reasoning and Acting

## Comparing Direct Prompting, Chain-of-Thought, and ReAct

---

## 1. Scenario

The scenario selected for this project is a **Student Course Fee Assistant**.

The assistant has access to course fee information stored in a local JSON file.

The course fees are:

| Course | Fee |
|---|---:|
| CS101 | ₹20,000 |
| AI202 | ₹18,000 |
| DS303 | ₹15,000 |

The main question used for comparison is:

> What is the total fee for CS101 and AI202 after applying a 10% scholarship?

The correct calculation is:

- CS101 = ₹20,000
- AI202 = ₹18,000
- Total = ₹38,000
- 10% scholarship = ₹3,800
- Final fee = ₹34,200

Three approaches are compared:

1. Direct Prompting
2. Chain-of-Thought
3. ReAct

---

# 2. Direct Prompting

## 2.1 Approach

Direct prompting gives the model the required information and asks it to answer the question directly.

No external tool is used.

The model receives the course fee data together with the question.

## 2.2 Example

Question:

> What is the total fee for CS101 and AI202 after applying a 10% scholarship?

The model receives:

```text
CS101 = ₹20,000
AI202 = ₹18,000