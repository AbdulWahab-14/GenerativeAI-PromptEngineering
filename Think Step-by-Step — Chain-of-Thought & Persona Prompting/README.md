# Week 2 Task 2: Chain-of-Thought (CoT) & Persona Prompting Comparison

## 1. Selected Problem
**Scenario:** A retail company sells 500 units of a product per month at $20 each with a 40% profit margin. If they lower the price by 10%, sales volume increases by 25%. Should the company make this price change to increase total monthly net profit?

---

## 2. Test 1: Plain Direct Prompt (No Persona or CoT)

**Prompt:**
> Should a company drop product prices by 10% from $20 if sales volume goes up by 25% from 500 units, assuming a 40% profit margin?

**Output:**
> Yes, lowering the price is a good idea. A 25% increase in sales volume will bring in significantly more customers, which boosts total revenue and helps cover your operating costs better overall.

---

## 3. Test 2: Chain-of-Thought + Persona Prompt

**Prompt:**
> You are a Senior Financial Analyst evaluating a retail pricing strategy. Think step-by-step before providing your final recommendation. Calculate the original total profit, the new unit price, the new cost per unit, the new sales volume, and the new total profit. Compare the net profits and state your decision.

**Output:**
> **Step 1: Baseline Metrics**
> * Original Selling Price: $20.00
> * Original Monthly Volume: 500 units
> * Original Revenue: 500 * $20 = $10,000
> * Profit Margin: 40% -> Profit per unit = $20 * 0.40 = $8.00
> * Unit Cost (COGS): $20 - $8 = $12.00
> * **Original Net Profit:** 500 units * $8.00 = **$4,000**
>
> **Step 2: Post-Discount Metrics**
> * New Selling Price (10% discount): $20 * 0.90 = $18.00
> * New Profit per Unit: $18.00 - $12.00 (COGS) = $6.00
> * New Monthly Volume (25% increase): 500 * 1.25 = 625 units
> * **New Net Profit:** 625 units * $6.00 = **$3,750**
>
> **Recommendation:**
> **Do NOT make the price change.** Although total revenue increases slightly ($11,250), the profit margin per unit compresses from $8.00 down to $6.00. This results in a net monthly profit **loss of $250** ($4,000 vs $3,750).

---

## 4. Analysis & Comparison

Combining Chain-of-Thought (CoT) with persona prompting fundamentally transformed the accuracy and reliability of the output. The direct prompt caused the model to fall back on superficial intuition, incorrectly assuming that higher sales volume automatically leads to higher net profits. By adopting the persona of a Senior Financial Analyst, the model prioritized financial precision over surface-level assumptions. Requiring a step-by-step reasoning chain forced the LLM to compute exact margin compressions sequentially before committing to a final conclusion, completely reversing the initial incorrect recommendation.
