GenerateContentResponse
│
├── text  ⚡ (ATAJO MÁS USADO)
│     └── str
│     → equivalente a:
│       candidates[0].content.parts[*].text (unido)
│
├── candidates (📦 RESPUESTAS COMPLETAS)
│     │
│     └── [0] Candidate
│           │
│           ├── content
│           │     ├── role → "model"
│           │     │
│           │     └── parts[]
│           │            │
│           │            ├── Part
│           │            │     ├── text 🟢
│           │            │     │     → respuesta normal
│           │            │     │
│           │            │     ├── function_call 🔵
│           │            │     │     ├── name
│           │            │     │     └── args
│           │            │     │
│           │            │     ├── function_response 🟣
│           │            │     │     → respuesta de tool (si la envías tú de vuelta)
│           │            │     │
│           │            │     └── inline_data 🟡
│           │            │           → imágenes / bytes (si aplica)
│           │            │
│           │            └── ...
│           │
│           ├── finish_reason
│           │       ├── "STOP"        → terminó normal
│           │       ├── "TOOL_USE"    → pidió función
│           │       ├── "MAX_TOKENS"
│           │       ├── "SAFETY"
│           │       └── "RECITATION"
│           │
│           ├── index
│           └── safety_ratings
│
├── usage_metadata ⚙️ (TOKENS)
│     ├── prompt_token_count
│     ├── candidates_token_count
│     ├── total_token_count
│     └── cached_content_token_count (si caching)
│
├── model_version
│     └── "gemini-2.5-flash"
│
└── 🧠 HELPERS (LO IMPORTANTE PARA TI)
      │
      ├── response.function_calls
      │     → lista directa de FunctionCall
      │
      ├── response.function_call
      │     → primer function call (atajo)
      │
      ├── response.parts
      │     → flatten de todos los parts
      │
      ├── response.candidates[0].content.parts
      │     → acceso manual (nivel bajo)
      │
      └── response.to_dict()
            → versión JSON completa del response