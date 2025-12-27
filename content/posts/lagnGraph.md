---
title: I built a news intelligence agent with LangGraph. I'm still not sure I needed the framework.
description: May take on the Lang stack
keywords: LangGraph, AI Agents
date: 2025-12-16
---
# I built a news intelligence agent with LangGraph. I'm still not sure I needed the framework.

After hearing about LangGraph in countless conversations (including interviews), I decided that enough was enough and start building.

## **What I Built:**

A news deep search system that:
- Orchestrates 35 parallel web searches
- Uses LLM agents to analyze, synthesize, and filter results
- Generates markdown news latter 

## **My Take After Building It:** 

LangGraph delivered typed state management and parallel execution helpers. But I kept thinking: I could've achieved this with Python's asyncio, dataclasses, and standard control flow.

The state graph? Essentially structured JSON with routing logic. That's the core abstraction.

Yes, LangGraph offers conveniences—automatic state merging, built-in visualization. But I'm not convinced the framework overhead pays for itself versus writing straightforward code.


## **Where LangGraph Makes Sense to Me:**

Team collaboration. If you're handing off code, a standardized framework. My asyncio + checkpointing approach? Requires walking through design decisions. LangGraph? Once your team knows the patterns, it should be easier to understand.