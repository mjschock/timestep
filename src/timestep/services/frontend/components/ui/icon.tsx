"use client";

import React from "react";
import { LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

interface IconProps extends React.HTMLAttributes<HTMLSpanElement> {
  icon: LucideIcon;
}

export function Icon({ icon: Icon, className, ...props }: IconProps) {
  return (
    <span suppressHydrationWarning className={cn("cursor-pointer", className)} {...props}>
      <Icon />
    </span>
  );
} 