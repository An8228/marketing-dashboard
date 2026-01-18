import React from "react";

type KpiCardProps = {
  title: string;
  value: string | number;
  subtitle?: string;
};

export function KpiCard({ title, value, subtitle }: KpiCardProps) {
  return (
    <div className="kpi-card">
      <div className="kpi-title">{title}</div>
      <div className="kpi-value">{value}</div>
      {subtitle && <div className="kpi-subtitle">{subtitle}</div>}
    </div>
  );
}
