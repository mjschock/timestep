"use client"

import { createContext, useContext, useEffect, useState } from "react"

type Theme = "dark" | "light"

type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}

type ThemeProviderState = {
  theme: Theme
  setTheme: (theme: Theme) => void
  isLoaded: boolean
}

const initialState: ThemeProviderState = {
  theme: "light",
  setTheme: () => null,
  isLoaded: false,
}

const ThemeProviderContext = createContext<ThemeProviderState>(initialState)

export function ThemeProvider({
  children,
  defaultTheme = "light",
  storageKey = "theme",
  ...props
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(defaultTheme)
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    const savedTheme = localStorage.getItem(storageKey)
    
    if (savedTheme && ["dark", "light"].includes(savedTheme)) {
      setTheme(savedTheme as Theme)
    }
    setIsLoaded(true)
  }, [storageKey])

  useEffect(() => {
    localStorage.setItem(storageKey, theme)

    if (theme === "dark") {
      document.documentElement.classList.add("dark")
    } else {
      document.documentElement.classList.remove("dark")
    }
  }, [theme, storageKey])

  const value = {
    theme,
    setTheme,
    isLoaded,
  }

  return (
    <ThemeProviderContext.Provider {...props} value={value}>
      {children}
    </ThemeProviderContext.Provider>
  )
}

export const useTheme = (): ThemeProviderState => {
  const context = useContext(ThemeProviderContext)

  if (context === undefined)
    throw new Error("useTheme must be used within a ThemeProvider")

  return context
} 